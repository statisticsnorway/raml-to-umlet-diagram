import pprint
import xml.etree.ElementTree as ET

class Utils():
    def printDict(self, dict):
        pp = pprint.PrettyPrinter(indent=4, compact=False)
        pp.pprint(dict)

    def printETree(self, eTree):
        #print(ET.tostring(eTree, encoding='utf8', method='xml'))
        print(ET.tostring(eTree, encoding='unicode', method='xml'))
        #ElementTree.dump(root)

    def printList(self, list):
        strList = ""
        for elem in list:
            strList += elem + "\n"
        print(strList)
