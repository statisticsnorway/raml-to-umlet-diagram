import yaml
from Config import Config
from Utils import Utils
from os import walk


class RamlObject():

    conf = Config()
    ramlPath = conf.ramlPath

    utils = Utils()


    def readAndCleanRamlFile(self, ramlFile):
        # Fjerner diverse "grums" fra raml-filen som ikke følger(?) yaml-syntaks.
        # Eksempel på linjer som fjernes:
        #    #%RAML 1.0 Library
        #    example: !include ../examples/_main/LogicalRecord_Person_1.json
        cleanedRaml = ""
        f = open(self.ramlPath + ramlFile, mode="r", encoding="utf-8")
        for line in f:
            if "#%RAML" in line or "example:" in line:
                None
            else:
                cleanedRaml = cleanedRaml + line
        f.close()
        return cleanedRaml

    def ramlFile2DictObject(self, ramlFile):
        # Konverterer raml (yaml) til Python dictionary object
        strRaml = self.readAndCleanRamlFile(ramlFile)
        ramlObjekt = yaml.load(strRaml, Loader=yaml.FullLoader)
        #for x, y in ramlObjekt.items():
        #  print(x, y, "\n")
        return ramlObjekt

    def getRamlFiles(self):
        for (dirpath, dirnames, filenames) in walk(self.ramlPath):
            return filenames

# RUN TEST
#ro = RamlObject()
#print(ro.getRamlFiles())
#ramlObjekt = ro.raml2DictObject("LogicalRecord.raml")
#ro.utils.printDict(ramlObjekt)
