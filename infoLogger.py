import accessories as ac
import os

class infoLogger(object):

    def __init__(self, fileName, subdir, writer):
        self.subdir = subdir
        self.hatiar = ac.accessories()
        self.inputFile = fileName
        self.writer = writer
        self.data = self.hatiar.getPanda(fileName)
        self.data['thread name'] = self.data['thread name'].str.replace('Thread-', '', case=False)
        self.hatiar.prettyPrint(self.data.columns)

    def writeInfo(self):
        self.writer.writeSheet(self.data, 'thread-info')

    def plotBar(self, keys, index, plotName):
        data = self.data[keys].set_index(index)
        self.writer.writeSheet(data, plotName)
        keys.remove(index[0])

        if len(data) <= 300:
            self.hatiar.printBar(data, index, keys, self.subdir+'\\'+plotName)
        else:
            dataList = self.hatiar.dataToChunkList(data, chunkSize=300)
            # path checker
            if not os.path.exists(self.subdir+'\\'+plotName):
                os.makedirs(self.subdir+'\\'+plotName)
            i=1
            for dataChunk in dataList:
                self.hatiar.printBar(dataChunk, index, keys, self.subdir+'\\'+plotName+'\\'+plotName+'-'+i.__str__())
                i += 1

    def plotBox(self, keys, index, plotName):
        data = self.data[keys]
        self.writer.writeSheet(data, plotName)
        self.hatiar.printBox(data, self.subdir+'\\'+plotName, index)
