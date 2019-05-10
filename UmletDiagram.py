import xml.etree.ElementTree as ET
from Config import Config
from Utils import Utils
from RamlObject import RamlObject
import time
from shutil import copyfile
import os


    # Example of format-tagged "PanelAttributes-text" in the Umlet diagram-file (.uxf):
        # */DataSet/*
        # -
        # --> IdentifiableArtefact
        # -
        # dataSetState: string(enum)
        #   - RAW_DATA, INPUT_DATA, PROCESSED_DATA, OUTPUT_DATA, DATA_PRODUCT, OTHER_DATA
        # dataExistsFromDate?: datetime
        # metadataSourcePath?: string
        #
        # bg=yellow
        # lt=.

class UmletDiagram():

    treeFile = None
    umletXmlTree = None

    conf = Config()
    umletPath = conf.umletPath
    #ramlPath = conf.ramlPath

    utils = Utils()

    ramlObj = RamlObject()
    ramlFiles = ramlObj.getRamlFiles()
    abstractRamlFiles = ramlObj.getAbstractRamlFiles()
    allRamlFiles = ramlObj.getAllRamlFiles()

    numOfNewRamlObjectsAdded = 0
    numOfUpdatedRamlObjects = 0


    def gsimNameToUmletTag(self, gsimName):
        # In the "panel attributes" in the Umlet-diagram-file the gsim object name is tagged like "*/gsim_object_name/*"
        return "*/" + gsimName + "/*"

    def getGsimName(self, ramlFileName):
        return ramlFileName.replace(".raml", "")

    def getRamlFileName(self, gsimName):
        return gsimName + ".raml"

    def readUmletXmlFile(self, fileName):
        self.treeFile = ET.parse(self.umletPath + fileName)
        self.umletXmlTree = self.treeFile.getroot()

# TODO: Trenger trolig ikke denne metoden ????
    def writeUMLetXmlFile(self, xml, fileName):
        xmlfile = open(self.umletPath + fileName + ".uxf", mode="w", encoding="utf-8")
        #xmlfile.write(xml.decode())
        xmlfile.write(xml)
        xmlfile.close()

# # TODO: Usikker på om denne er nødvendig????
#     def writeUMLetXmlFile(self, fileName):
#         #self.treeFile.write(self.umletPath + 'NY_GSIM_physical_model.uxf')
#         None

    def updateUmletDiagramNote(self):
        umletNote = self.umletXmlTree.find('.//*[id="UMLNote"]/panel_attributes')
        umletNote.text = \
          "*GSIM Physical Data Model - RAML Schema*\n" \
          + "Version: " + time.strftime("%Y-%m-%d, %H:%M") + "\n" \
          + "fontsize=14"

    def gsimObjectExistInUmletDiagram(self, gsimName):
        panelAttributesForAllUmletClasses = self.getPanelAttributesForAllUmletClasses()
        for panel_attributes in panelAttributesForAllUmletClasses:
            if self.gsimNameToUmletTag(gsimName) in panel_attributes.text:
                return True
        return False

    def getPanelAttributesForAllUmletClasses(self):
        #self.readUmletXmlFile()
        # Find "panel_attributes" (elements) for all the "UmlClass"-objects in the Umlet-diagram.
        return self.umletXmlTree.findall('.//*[id="UMLClass"]/panel_attributes')

    def getPanelAttributesForUmletClassByGsimName(self, gsimName):
        panelAttributesForAllUmletClasses = self.getPanelAttributesForAllUmletClasses()
        for panel_attributes in panelAttributesForAllUmletClasses:
            if self.gsimNameToUmletTag(gsimName) in panel_attributes.text:
                # print(panel_attributes.text)
                return panel_attributes

    def getUmletPanelAttributeDetail(self, umletPanelAttribute, umletDetail):
        panelLines = umletPanelAttribute.text.split("\n")
        for line in panelLines:
            if umletDetail+"=" in line or umletDetail+" =" in line:
                return line
        return ""

# TODO: Umlet-relasjoner (piler)!!!!
    def createPanelAttributesForUmletClass(self, gsimName):
        umletAttr = ""
        ramlObject = self.ramlObj.ramlFile2DictObject(gsimName + ".raml")
        for ramlTypes in ramlObject["types"]:
            umletAttr += "*/" + str(ramlTypes) + "/*\n"  # E.g. "LogicalRecord"  (* * = bold text)
            umletAttr += "-\n"  # Horizontal line in UMLet-diagram.
            if "type" in ramlObject["types"][ramlTypes]:
                ramlUses = str(ramlObject["types"][ramlTypes]["type"]) \
                            .replace("'", "").replace("[", "").replace("]", "").split(",")
                for ru in ramlUses:
                    umletAttr += "--> " + ru.strip().split(".")[0] + "\n"  # E.g. inherit "IdentifiableArtefact"
        umletAttr += "-\n"  # Horizontal line in UMLet-diagram.

        ramlProperties = ramlObject["types"][ramlTypes]["properties"]  # E.g. "identifierComponent", "measureComponent", ...
        if ramlProperties:
            for ramlProperty in ramlProperties:
                umletAttr += ramlProperty + ": "  #(* * = bold text)
                if "(Link.types)" in ramlObject["types"][ramlTypes]["properties"][ramlProperty]:
                    # identifierComponents: link[] (IdentifierComponent)
                    ramlPropType = str(ramlObject["types"][ramlTypes]["properties"][ramlProperty]["type"])
                    ramlPropType = ramlPropType.replace("string", "")
                    ramlPropLinkTypes = str(ramlObject["types"][ramlTypes]["properties"][ramlProperty]["(Link.types)"])
                    ramlPropLinkTypes = ramlPropLinkTypes.replace("[","").replace("]","").replace("'","")
                    umletAttr += "link" + ramlPropType + ": (" + ramlPropLinkTypes + ")"
# TODO: Umlet-relasjoner (piler):
                    #self.umletRelations.append(self.createUMLetRelation(str(ramlTypes) + "_" + ramlPropLinkTypes ,10, (self.relationCount*60)+120))
                    #self.relationCount += 1
                elif "type" in ramlObject["types"][ramlTypes]["properties"][ramlProperty]:
                    ramlPropType = ramlObject["types"][ramlTypes]["properties"][ramlProperty]["type"]  # E.g. "string"
                    umletAttr += ramlPropType
                    if "enum" in ramlObject["types"][ramlTypes]["properties"][ramlProperty]:
                        ramlPropEnum = ramlObject["types"][ramlTypes]["properties"][ramlProperty]["enum"]  # E.g. "enum --> IDENTIFIER, ATTRIBUTE, MEASURE"
                        umletAttr += "(enum)\n  - " + ", ".join(ramlPropEnum)
                if "displayName" in ramlObject["types"][ramlTypes]["properties"][ramlProperty]:
                    ramlPropDisplayName = ramlObject["types"][ramlTypes]["properties"][ramlProperty]["displayName"]
                    #print(ramlPropDisplayName)
                if "description" in ramlObject["types"][ramlTypes]["properties"][ramlProperty]:
                    ramlPropDescription = ramlObject["types"][ramlTypes]["properties"][ramlProperty]["description"]
                    #print(ramlPropDescription)
                umletAttr += "\n"
        if self.getRamlFileName(gsimName) in self.abstractRamlFiles:
            umletAttr += "\n"
            umletAttr += "lt=." # dashed borderline in the Umlet-diagram
        return umletAttr


    def updatePanelAttributesForUmletClassByGsimName(self, gsimName):
        self.numOfUpdatedRamlObjects += 1
        # Get existing panel-attributes for this Umlet diagram-object
        panel_attributes = self.getPanelAttributesForUmletClassByGsimName(gsimName)
        backGroundColor = self.getUmletPanelAttributeDetail(panel_attributes, "bg")
        #borderLineType = self.getUmletPanelAttributeDetail(panel_attributes, "lt")
        # Update with new metadata from the GSIM RAML-file
        umletPanelAttr = self.createPanelAttributesForUmletClass(gsimName)
        umletPanelAttr += "\n" + backGroundColor
        #umletPanelAttr += "\n" + borderLineType
        panel_attributes.text = umletPanelAttr
        #self.treeFile.write(self.umletPath + 'NY_3_GSIM_physical_model.uxf')

    def addNewUmletClassInDiagram(self, gsimName):
        # Example XML of UML class in Umlet diagram file:
          # <element>
          #   <id>UMLClass</id>
          #   <coordinates>
          #     <x>260</x>
          #     <y>10</y>
          #     <w>250</w>
          #     <h>100</h>
          #   </coordinates>
          #   <panel_attributes>*/DataSet/*
          #   ......
          #   </panel_attributes>
          #   <additional_attributes />
          # </element>
        self.numOfNewRamlObjectsAdded += 1
        umletClassElement = ET.Element("element")
        id = ET.SubElement(umletClassElement, "id")
        id.text = "UMLClass"
        panel_attributes = ET.SubElement(umletClassElement, "panel_attributes")
        panel_attributes.text = self.createPanelAttributesForUmletClass(gsimName)
        additional_attributes = ET.SubElement(umletClassElement, "additional_attributes")
        umletCoordinates = ET.SubElement(umletClassElement, "coordinates")
        xCoord = ET.SubElement(umletCoordinates, "x")
        xCoord.text = str(10 + (self.numOfNewRamlObjectsAdded * 5))
        yCoord = ET.SubElement(umletCoordinates, "y")
        yCoord.text = str(50 + (self.numOfNewRamlObjectsAdded * 20))
        wCoord = ET.SubElement(umletCoordinates, "w")
        wCoord.text = "250"
        hCoord = ET.SubElement(umletCoordinates, "h")
        hCoord.text = "100"
        self.umletXmlTree.insert(2, umletClassElement)


# TODO:
    def generateUmletDiagram(self, umletFileName):
        self.readUmletXmlFile(umletFileName)

        for ramlFile in self.allRamlFiles:
            gsimName = self.getGsimName(ramlFile)
            if self.gsimObjectExistInUmletDiagram(gsimName):
                self.updatePanelAttributesForUmletClassByGsimName(gsimName)
            else:
                self.addNewUmletClassInDiagram(gsimName)
        # TODO: 1. backup av gammle fil (old + filnavn)
        # TODO: Sette riktig filnavn på nytt diagram!
        self.updateUmletDiagramNote()
        # Backup Umlet diagram file before write.
        copyfile(self.umletPath + umletFileName, self.umletPath + umletFileName + "_" + time.strftime("%Y%m%d%H%M%S"))
        self.treeFile.write(self.umletPath + umletFileName)
        print("\nUmlet diagram: " + os.path.abspath(self.umletPath + umletFileName))
        print(".. " + str(self.numOfNewRamlObjectsAdded) + " new GSIM/RAML class object(s) added to Umlet diagram.")
        print(".. " + str(self.numOfUpdatedRamlObjects) + " existing GSIM/RAML class object(s) updated in Umlet diagram.")

# RUN TEST
ud = UmletDiagram()
ud.generateUmletDiagram("GSIM_physical_model.uxf")
#ud.generateUmletDiagram("dummy")
#ud.readUmletXmlFile("GSIM_physical_model.uxf")
#print(ud.gsimObjectExistInUmletDiagram("LogicalRecord"))
#print(ud.getPanelAttributesForUmletClassByGsimName("LogicalRecord"))
#ud.updatePanelAttributesForUmletClassByGsimName("LogicalRecord")
