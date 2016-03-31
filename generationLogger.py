import accessories as ac
import os
class generationLogger(object):

    def __init__(self, fileName, subdir, writer):

        self.subdir = subdir
        self.hatiar = ac.accessories()
        self.writer = writer
        self.inputFile = fileName
        self.data = self.hatiar.getPanda(fileName)

        # self.hatiar.prettyPrint(self.data)

    def plotBar(self, keys, index, sheetName):

        data = self.hatiar.getPanda(self.inputFile)
        data = data[keys].set_index(index)
        # self.hatiar.prettyPrint(data)
        self.writer.writeSheet(data, sheetName)
        keys.remove(index[0])
        self.hatiar.printBar(data, index, keys, self.subdir+'\\'+sheetName)

    def writeGroup(self):

        data = self.hatiar.getPanda(self.inputFile)
        self.writer.writeSheet(data.cov(), 'covariance')
        self.writer.writeSheet(data.corr(), 'pearson-correlation')
        self.writer.writeSheet(data.corr(method='spearman'), 'spearman_correlation')
        self.writer.writeSheet(data.pct_change(), 'percent_change')
        print('group data written for '+self.subdir+'\\'+self.inputFile)

