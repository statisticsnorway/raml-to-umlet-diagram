import yaml
import itertools
from Config import Config
from Utils import Utils
from os import walk
#from os import listdir


class RamlObject():

    conf = Config()
    ramlPath = conf.ramlPath
    ramlAbstractPath = conf.ramlAbstractPath

    utils = Utils()


    def readAndCleanRamlFile(self, ramlFile):
        # Fjerner diverse "grums" fra raml-filen som ikke følger(?) yaml-syntaks.
        # Eksempel på linjer som fjernes:
        #    #%RAML 1.0 Library
        #    example: !include ../examples/_main/LogicalRecord_Person_1.json
        cleanedRaml = ""
        path = None
        #print(ramlFile)
        if ramlFile in self.getAbstractRamlFiles():
            #print("abstract" + ramlFile)
            path = self.ramlAbstractPath
        else:
            path = self.ramlPath
        f = open(path + ramlFile, mode="r", encoding="utf-8")
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
        #for (dirpath, dirnames, filenames) in walk(self.ramlPath):
        return next(walk(self.ramlPath))[2]  # files only (not sub-directories)

    def getAbstractRamlFiles(self):
        #for (dirpath, dirnames, filenames) in walk((self.ramlAbstractPath):
        return next(walk(self.ramlAbstractPath))[2]  # files only (not sub-directories)

    def getAllRamlFiles(self):
        ramlFiles = self.getRamlFiles()
        abstractRamlFiles = self.getAbstractRamlFiles()
        #allFiles = list(itertools.chain(ramlFiles, abstractRamlFiles))
        allFiles = [*ramlFiles, *abstractRamlFiles]  # merge file lists
        return allFiles


# RUN TEST
#ro = RamlObject()
#files = ro.getAllRamlFiles()
#ro.utils.printList(files)
#ramlObjekt = ro.raml2DictObject("LogicalRecord.raml")
#ro.utils.printDict(ramlObjekt)
