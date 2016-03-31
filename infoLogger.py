import accessories as ac
import os

class infoLogger(object):

    def __init__(self, fileName, subdir, writer):

        self.subdir = subdir
        self.hatiar = ac.accessories()
        self.inputFile = fileName
        self.writer = writer
        self.data = self.hatiar.getPanda(fileName)

    def writeInfo(self):

        self.writer.writeSheet(self.data, 'ThreadInfo')

    def plotBar(self, keys, index, plotName):

        data = self.data[keys].set_index(index)
        self.writer.writeSheet(data, plotName)
        keys.remove(index[0])
        self.hatiar.printBar(data, index, keys, self.subdir+'\\'+plotName)

    def plotBox(self, keys, index, plotName):

        data = self.data[keys]
        self.writer.writeSheet(data, plotName)
        self.hatiar.printBox(data, self.subdir+'\\'+plotName, index)