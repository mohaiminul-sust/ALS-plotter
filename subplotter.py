import os
from matplotlib import style
import generationLogger as gl
import excelWriter as ew
import infoLogger as il
import alsPlotter as ap

path = 'ALS_data'

# using plotting style for pandas
style.use('ggplot')

for subdir, dirs, files in os.walk(path):
    if not os.path.exists(subdir + '\\plots'):
        if 'plots' not in subdir:
            print('.......................' + subdir + '........................')
            os.makedirs(subdir + '\\plots')

    for file in files:
        if file == 'ALS_data.csv':
            writer = ew.excelWriter(subdir + '\\plots\\als_logger.xlsx')
            alspl = ap.alsPlotter(fileName=subdir + '\\' + file, subdir=subdir + '\\plots', writer=writer)

            # write als data to excel
            alspl.writeAlsData()

            # plot bar graphs
            alspl.plotBar(['number_of_run', 'total_thread', 'total_male', 'total_female'], ['number_of_run'],
                          'runtime vs total_male_female')
            alspl.plotBar(['number_of_run', 'copy_dna_number', 'total_thread'], ['number_of_run'],
                          'runtime vs total_copy_dna_num')
            alspl.plotBar(['number_of_run', 'copy_dna_number'], ['number_of_run'], 'runtime vs copy_dna_num')
            alspl.plotBar(['number_of_run', 'time'], ['number_of_run'], 'runtime vs time')
            alspl.plotBar(['number_of_run', 'latest_generation', 'time'], ['number_of_run'],
                          'runtime vs latest_gen_time')
            alspl.plotBar(['number_of_run', 'latest_generation'], ['number_of_run'], 'runtime vs latest_gen')
            alspl.plotBar(['number_of_run', 'total_thread'], ['number_of_run'], 'runtime vs total_thread')

            writer.saveWriter()

        if file == 'Generation_log.csv':
            writer = ew.excelWriter(subdir + '\\plots\\gen_logger.xlsx')
            genLog = gl.generationLogger(fileName=subdir + '\\' + file, subdir=subdir + '\\plots', writer=writer)
            genLog.plotBar(['generation_number', 'offsprings_per_generation'], ['generation_number'],
                           'gen vs offspring')
            genLog.plotBar(['generation_number', 'male_offsprings_per_generation'], ['generation_number'],
                           'gen vs male_offspring')
            genLog.plotBar(['generation_number', 'female_offsprings_per_generation'], ['generation_number'],
                           'gen vs female_offspring')
            genLog.plotBar(['generation_number', 'female_offsprings_per_generation', 'male_offsprings_per_generation'],
                           ['generation_number'], 'gen vs male_female_offspring')
            genLog.plotBar(['generation_number', 'duration'], ['generation_number'], 'gen vs duration_nano')

            genLog.writeGroup()
            writer.saveWriter()

        if file == 'ThreadInfo.csv':
            writer = ew.excelWriter(subdir + '\\plots\\thread_logger.xlsx')
            threadLog = il.infoLogger(fileName=subdir + '\\' + file, subdir=subdir + '\\plots', writer=writer)

            threadLog.writeInfo()
            threadLog.plotBar(['thread name', 'total move'], ['thread name'], 'move-per-thread')
            threadLog.plotBar(['thread name', 'alive_time'], ['thread name'], 'time-per-thread')
            threadLog.plotBar(['thread name', 'total food count', 'total poison count'], ['thread name'],
                              'food-poison-per-thread')

            writer.saveWriter()
