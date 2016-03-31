import pandas as pd

class excelWriter(object):

    def __init__(self, fileName):
        writer = pd.ExcelWriter(fileName)
        self.writer = writer
        self.fileName = fileName
        print('writer initialized')

    def writeSheet(self, data, sheetName):
        data.to_excel(self.writer, sheetName)
        print(sheetName+' data saved !')

    def saveWriter(self):
        self.writer.save()
        print(self.fileName+' saved !')