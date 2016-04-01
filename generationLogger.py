import accessories as ac
class generationLogger(object):

    def __init__(self, fileName, subdir, writer):

        self.subdir = subdir
        self.hatiar = ac.accessories()
        self.writer = writer
        self.inputFile = fileName
        self.data = self.hatiar.getPanda(fileName)
        print(self.data.columns)

    def plotBar(self, keys, index, sheetName):

        data = self.data[keys].set_index(index)
        self.writer.writeSheet(data, sheetName)
        keys.remove(index[0])
        self.hatiar.printBar(data, index, keys, self.subdir+'\\'+sheetName)

    def writeGroup(self):

        self.writer.writeSheet(self.data.cov(), 'covariance')
        self.writer.writeSheet(self.data.corr(), 'pearson-correlation')
        self.writer.writeSheet(self.data.corr(method='spearman'), 'spearman_correlation')
        self.writer.writeSheet(self.data.pct_change(), 'percent_change')
        print('group data written for '+self.subdir+'\\'+self.inputFile)