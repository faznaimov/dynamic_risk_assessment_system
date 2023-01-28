'''
Script that tracks f1 score of the model

Author: Faz Naimov
Date: 1/26/2023
'''

import pandas as pd
import pickle
import os
from sklearn import metrics
import json

# Load config.json and get path variables
with open('config.json', 'r') as f:
    config = json.load(f)

test_data_path = os.path.join(config['test_data_path'])
model_path = os.path.join(config['output_model_path'])


# Function for model scoring
def score_model(data_path, overwrite=True):
    # this function should take a trained model, load test data, and calculate an F1 score for the model relative to the test data
    # it should write the result to the latestscore.txt file
    with open(model_path + '/trainedmodel.pkl', 'rb') as file:
        model = pickle.load(file)

    test_data = pd.read_csv(data_path)
    X = test_data.loc[:, ['lastmonth_activity', 'lastyear_activity',
                          'number_of_employees']].values.reshape(-1, 3)
    y = test_data['exited'].values.reshape(-1, 1).ravel()

    predicted = model.predict(X)
    f1score = metrics.f1_score(predicted, y)

    if overwrite:
        with open(model_path + '/latestscore.txt', 'w') as f:
            f.write(str(f1score))

    return f1score


if __name__ == '__main__':
    score_model(test_data_path + '/testdata.csv', overwrite=True)
