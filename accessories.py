import pandas as pd
import pprint as pp
import matplotlib.pyplot as plt

class accessories(object):

    # get data using panda from csv
    def getPanda(self ,fileName):
        panda = pd.read_csv(fileName)
        panda.columns = panda.columns.str.strip()
        panda.columns = panda.columns.str.lower()
        return panda

    def getDescription(self, data):
        return data.describe()

    def prettyPrint(self, data):
        return pp.pprint(data, width='1')

    def printBar(self, data, xlabel, ylabel, name):
        figBar = data.plot.bar(stacked=False, figsize=(40, 10))
        figBar.set_xlabel(', '.join(xlabel))
        figBar.set_ylabel(', '.join(ylabel))
        figBar.get_figure().savefig(name+".png")
        print('saved '+name+'.png...')
        plt.close('all')

    def printBox(self, data, name, index):
        plt.tight_layout()
        figBar = data.plot.box(by=index)
        figBar.get_figure().savefig(name+".png")
        print('saved '+name+'.png...')
        plt.close('all')

    # input - data: a Dataframe, chunkSize: the chunk size
    # output - a list of DataFrame
    # purpose - splits the DataFrame into smaller of max size chunkSize (last is smaller)
    def dataToChunkList(self, data,  chunkSize = 300):
        dataList = list()
        numberChunks = len(data) // chunkSize + 1
        for i in range(numberChunks):
            dataList.append(data[i*chunkSize:(i+1)*chunkSize])
        return dataList