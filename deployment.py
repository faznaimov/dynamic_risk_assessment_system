'''
Script that copies model and other files to deployment.

Author: Faz Naimov
Date: 1/26/2023
'''

import os
import json
import shutil


# Load config.json and correct path variable
with open('config.json', 'r') as f:
    config = json.load(f)

dataset_csv_path = os.path.join(config['output_folder_path'])
model_path = os.path.join(config['output_model_path'])
prod_deployment_path = os.path.join(config['prod_deployment_path'])


# function for deployment
def store_model_into_pickle(copy_path):
    # copy the latest pickle file, the latestscore.txt value, and the
    # ingestedfiles.txt file into the deployment directory
    shutil.copy(model_path + '/trainedmodel.pkl', copy_path)
    shutil.copy(model_path + '/latestscore.txt', copy_path)
    shutil.copy(dataset_csv_path + '/ingestedfiles.txt', copy_path)


if __name__ == '__main__':
    store_model_into_pickle(prod_deployment_path + '/')
