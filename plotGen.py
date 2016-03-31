# plot generator class

class plotGen(object):

    def __init__(self, hatiar, writer, inputFile):

        self.hatiar = hatiar
        self.writer = writer
        self.inputFile = inputFile
        print('Plot generator initialized')

    def printBar(self, keys, index, sheetName):

        data = self.hatiar.getPanda(self.inputFile)
        data = data[keys].set_index(index)
        # self.hatiar.prettyPrint(data)
        self.writer.writeSheet(data, sheetName)
        keys.remove(index[0])
        self.hatiar.printBar(data, index, keys, sheetName)
