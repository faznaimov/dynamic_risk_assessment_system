'''
Script to ingest data, merge it and create final data.

Author: Faz Naimov
Date: 1/24/2022
'''
import pandas as pd
import os
import json


# Load config.json and get input and output paths
with open('config.json', 'r') as f:
    config = json.load(f)

input_folder_path = config['input_folder_path']
output_folder_path = config['output_folder_path']


# Function for data ingestion
def merge_multiple_dataframe():

    filenames = os.listdir(os.getcwd() + '/' + input_folder_path)

    df_list = pd.DataFrame()
    files = []

    for each_filename in filenames:
        if '.csv' in each_filename:
            df1 = pd.read_csv(
                os.getcwd() +
                '/' +
                input_folder_path +
                '/' +
                each_filename)
            df_list = df_list.append(df1)
            files.append(each_filename)

    output_df = df_list.drop_duplicates()
    output_df.to_csv(output_folder_path + '/finaldata.csv', index=False)

    with open(output_folder_path + '/ingestedfiles.txt', 'w') as f:
        f.write(', '.join(files))


if __name__ == '__main__':
    merge_multiple_dataframe()
