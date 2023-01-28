'''
Script that creates confusion matrix

Author: Faz Naimov
Date: 1/27/2023
'''

import pandas as pd
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import json
import os
from diagnostics import model_predictions


# Load config.json and get path variables
with open('config.json', 'r') as f:
    config = json.load(f)

test_data_path = os.path.join(config['test_data_path'])


# Function for reporting
def score_model():
    y_test_preds = model_predictions()
    test_data = pd.read_csv(test_data_path + '/testdata.csv')
    y_test = test_data['exited'].values.reshape(-1, 1).ravel()

    # calculate a confusion matrix using the test data and the deployed model
    # write the confusion matrix to the workspace
    plt.figure('figure', figsize=(5, 5))
    plt.text(0.01, 0.7, str(classification_report(y_test, y_test_preds)),
             {'fontsize': 10}, fontproperties='monospace')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('images/confusionmatrix.png')


if __name__ == '__main__':
    score_model()
