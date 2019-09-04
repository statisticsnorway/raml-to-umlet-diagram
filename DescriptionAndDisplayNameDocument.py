from Config import Config

class DescriptionAndDisplayNameDocument():

    docList = []

    config = Config()

    def addDocForObject(self, objetDoc):
        self.docList.append(objetDoc)

    def writeDocAsMdFile(self):
        f = open(self.config.umletPath + "PhysicalDataModelDetails.md", "w", encoding='utf-8')
        for doc in self.docList:
            #print(doc, end="")
            f.write(doc)
        f.close()
