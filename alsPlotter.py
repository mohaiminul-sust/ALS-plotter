import accessories as ac

class alsPlotter(object):

    def __init__(self, fileName, subdir, writer):
        self.fileName = fileName
        self.subdir = subdir
        self.writer = writer
        self.hatiar = ac.accessories()
        self.data = self.hatiar.getPanda(fileName)
        self.hatiar.prettyPrint(self.data.columns)

    def plotBar(self, keys, index, plotName):
        data = self.data[keys].set_index(index)
        self.writer.writeSheet(data, plotName)
        keys.remove(index[0])
        self.hatiar.printBar(data, index, keys, self.subdir+'\\'+plotName)


    def writeAlsData(self):
        self.writer.writeSheet(self.hatiar.getDescription(self.data), 'description')
        self.writer.writeSheet(self.data.cov(), 'covariance')
        self.writer.writeSheet(self.data.corr(), 'pearson-correlation')
        self.writer.writeSheet(self.data.corr(method='spearman'), 'spearman-correlation')
        self.writer.writeSheet(self.data.pct_change(), 'percent-change')
        print("saved ALS_data to excel...")
