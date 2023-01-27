'''
Script that trains the model

Author: Faz Naimov
Date: 1/26/2022
'''

import pandas as pd
import pickle
import os
from sklearn.linear_model import LogisticRegression
import json

# Load config.json and get path variables
with open('config.json', 'r') as f:
    config = json.load(f)

dataset_csv_path = os.path.join(config['output_folder_path'])
model_path = os.path.join(config['output_model_path'])


# Function for training the model
def train_model():

    # data preprocessing
    trainingdata = pd.read_csv(dataset_csv_path + '/finaldata.csv')
    X = trainingdata.loc[:,
                         ['lastmonth_activity',
                          'lastyear_activity',
                          'number_of_employees']].values.reshape(-1,
                                                                 3)
    y = trainingdata['exited'].values.reshape(-1, 1).ravel()

    # use this logistic regression for training
    logit = LogisticRegression(
        C=1.0,
        class_weight=None,
        dual=False,
        fit_intercept=True,
        intercept_scaling=1,
        l1_ratio=None,
        max_iter=100,
        n_jobs=None,
        penalty='l2',
        random_state=0,
        solver='liblinear',
        tol=0.0001,
        verbose=0,
        warm_start=False)

    # fit the logistic regression to your data
    model = logit.fit(X, y)
    # write the trained model to your workspace in a file called
    # trainedmodel.pkl
    pickle.dump(model, open(model_path + '/trainedmodel.pkl', 'wb'))


if __name__ == '__main__':
    train_model()
