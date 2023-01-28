'''
Module containg diagnostics functions

Author: Faz Naimov
Date: 1/26/2023
'''

import pandas as pd
import timeit
import os
import json
import pickle

# Load config.json and get environment variables
with open('config.json', 'r') as f:
    config = json.load(f)

dataset_csv_path = os.path.join(config['output_folder_path'])
test_data_path = os.path.join(config['test_data_path'])
model_path = os.path.join(config['prod_deployment_path'])

# Function to get model predictions


def model_predictions():
    # read the deployed model and a test dataset, calculate predictions
    with open(model_path + '/trainedmodel.pkl', 'rb') as file:
        model = pickle.load(file)
    # read data
    test_data = pd.read_csv(test_data_path + '/testdata.csv')
    X = test_data.loc[:, ['lastmonth_activity', 'lastyear_activity',
                          'number_of_employees']].values.reshape(-1, 3)
    # predict
    predictions = model.predict(X)
    return predictions

# Function to get summary statistics


def dataframe_summary():
    stats = dict()
    dataframe = pd.read_csv(dataset_csv_path + '/finaldata.csv')
    for col in [
        'lastmonth_activity',
        'lastyear_activity',
            'number_of_employees']:
        mean = dataframe[col].mean()
        median = dataframe[col].median()
        std = dataframe[col].std()
        stats[col] = [mean, median, std]
    return stats

# Function to count NA


def count_na():
    dataframe = pd.read_csv(dataset_csv_path + '/finaldata.csv')
    nas = list(dataframe.isna().sum())
    napercents = [nas[i] / len(dataframe.index) for i in range(len(nas))]
    return napercents


# Function to get timings
def execution_time():
    # calculate timing of training.py and ingestion.py
    starttime = timeit.default_timer()
    os.system('python training.py')
    training = timeit.default_timer() - starttime

    starttime = timeit.default_timer()
    os.system('python ingestion.py')
    ingestion = timeit.default_timer() - starttime
    return [training, ingestion]


# Function to check dependencies
def outdated_packages_list():
    # get a list of
    return os.system('pip list --outdated')
