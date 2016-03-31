import os
from matplotlib import style
import generationLogger as gl
import excelWriter as ew
import infoLogger as il

path = 'ALS_data'

# using plotting style for pandas
style.use('ggplot')

for subdir, dirs, files in os.walk(path):

    if not os.path.exists(subdir+'\\plots'):
        if subdir != 'ALS_data':
            os.makedirs(subdir+'\\plots')

    for file in files:
        # print(file)
        if(file == 'Generation_log.csv'):

            writer = ew.excelWriter(subdir+'\\plots\\genLogger.xlsx')
            genLog = gl.generationLogger(subdir+'\\'+file, subdir+'\\plots', writer)
            genLog.plotBar(['generation_number', 'offsprings_per_generation'], ['generation_number'], 'gen vs offspring')
            genLog.plotBar(['generation_number', 'male_offsprings_per_generation'], ['generation_number'], 'gen vs male_offspring')
            genLog.plotBar(['generation_number', 'female_offsprings_per_generation'], ['generation_number'], 'gen vs female_offspring')
            genLog.plotBar(['generation_number', 'female_offsprings_per_generation', 'male_offsprings_per_generation'], ['generation_number'], 'gen vs male_female_offspring')
            genLog.plotBar(['generation_number', 'duration'], ['generation_number'], 'gen vs duration_nano')

            genLog.writeGroup()
            writer.saveWriter()

        if(file == 'ThreadInfo.csv'):

            writer = ew.excelWriter(subdir+'\\plots\\threadLogger.xlsx')
            threadLog = il.infoLogger(subdir+'\\'+file, subdir+'\\plots', writer)

            threadLog.writeInfo()
            threadLog.plotBar(['thread name', ' total move'], ['thread name'], 'move-per-thread')
            threadLog.plotBar(['thread name', 'alive_time'], ['thread name'], 'time-per-thread')
            threadLog.plotBar(['thread name', 'total food count ', ' total poison count '], ['thread name'], 'food-poison-per-thread')

            # threadLog.plotBox(['thread name', 'gendar'], 'gendar', 'threads-per-gender')
            # threadLog.plotBox(['thread name', ' dna'], ' dna', 'threads-per-dna')
            # threadLog.plotBox(['thread name', 'genaration_no'], 'genaration_no', 'boxplot-gen')

            writer.saveWriter()
