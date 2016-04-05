import accessories as ac
import os
class generationLogger(object):

    def __init__(self, fileName, subdir, writer):
        self.subdir = subdir
        self.hatiar = ac.accessories()
        self.writer = writer
        self.inputFile = fileName
        self.data = self.hatiar.getPanda(fileName)
        self.hatiar.prettyPrint(self.data.columns)

    def plotBar(self, keys, index, plotName):
        data = self.data[keys].set_index(index)
        self.writer.writeSheet(data, plotName)
        keys.remove(index[0])

        if len(data) <= 300:
            self.hatiar.printBar(data, index, keys, self.subdir+'\\'+plotName)
        else:
            dataList = self.hatiar.dataToChunkList(data, chunkSize=300)
            if not os.path.exists(self.subdir+'\\'+plotName):
                os.makedirs(self.subdir+'\\'+plotName)
            i=1
            for dataChunk in dataList:
                self.hatiar.printBar(dataChunk, index, keys, self.subdir+'\\'+plotName+'\\'+plotName+'-'+i.__str__())
                i += 1

    def writeGroup(self):
        self.writer.writeSheet(self.hatiar.getDescription(self.data), 'description')
        self.writer.writeSheet(self.data.cov(), 'covariance')
        self.writer.writeSheet(self.data.corr(), 'pearson-correlation')
        self.writer.writeSheet(self.data.corr(method='spearman'), 'spearman-correlation')
        self.writer.writeSheet(self.data.pct_change(), 'percent-change')
        print('group data written for '+self.subdir+'\\'+self.inputFile)