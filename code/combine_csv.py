##Created by Vivek Muralidharan on 2021/12/05
##Script to combine data from csv files in a specific folder and output required fields

#Importing required libraries
import pandas as pd
import os
import glob
import re
import logging
import sys

log_path = sys.argv[3]

log_file_name = 'combine_csv.log'

log_nm = os.path.join(log_path,log_file_name)

logging.basicConfig(level=logging.INFO
                    , filemode='a'
                    , format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s'
                    , filename=log_nm)

#Function to combine csv files in the specified folder
def combine_csv(src_path):
    files = glob.glob(src_path + '/*.csv')

    lst = []

    for filename in files:
        df = pd.read_csv(filename, names = ['Source IP','Counts','Events per second'], header=0)
        
        #Use regular expression to capture Environment value
        df['Environment']=re.sub(r'(.*?)\s*[0-9]*.csv', r'\1', os.path.basename(filename))
        
        #Append dataframes(for each file) to list
        lst.append(df)
    
    #Combine dataframes inside list to a single dataframe
    df2 = pd.concat(lst, axis=0, ignore_index=True)
    
    return df2


#Function to remove duplicates based on "Source IP" and "Environment"
def remove_duplicates(df):
    df_final=df.loc[:,['Source IP','Environment']]
    df_final.drop_duplicates(['Source IP','Environment'], keep = 'first', inplace = True)
    
    return df_final


#Function to write csv output
def generate_csv(df, out_file):
    df.to_csv(out_file, index=None)


if __name__ == '__main__':
    try:
        logger = logging.getLogger()
        
        logger.error('Debugging')
        
        #Defining file paths
        src_path = sys.argv[1]

        logger.info('Source File Path: ' + src_path)

        out_file = sys.argv[2]

        logger.info('Target File: ' + out_file)
        
        #Calling functions
        logger.info('\n********************\n' + 'Combining Source Files...')
        df2 = combine_csv(src_path)
        logger.info('Source Files Combined Successfully!' + '\n********************')
    
        logger.info('\n********************\n' + 'Removing Duplicate Entries...')
        df_final = remove_duplicates(df2)
        logger.info('Duplicate Entries Removed Successfully!' + '\n********************')
    
        logger.info('\n********************\n' + 'Generating Combined.csv file...')
        generate_csv(df_final, out_file)
        logger.info('Combined.csv Generated Successfully!\n' + out_file + '\n********************')
        
    except BaseException as err:
        logger.exception('ERROR: ' + str(err))
        