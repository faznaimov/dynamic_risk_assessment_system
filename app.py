'''
Flask app

Author: Faz Naimov
Date: 1/27/2023
'''

from flask import Flask, render_template
from diagnostics import *
from scoring import score_model

# Set up variables for use in our script
app = Flask(__name__)
app.secret_key = '1652d576-484a-49fd-913a-6879acfa6ba4'


@app.route('/')
def index():
    return render_template('index.html')

# Prediction Endpoint


@app.route("/prediction", methods=['GET', 'OPTIONS'])
def predict():
    # call the prediction function you created in Step 3
    pred = model_predictions()
    return f'Predictions of test data: {pred.tolist()}'

# Scoring Endpoint


@app.route("/scoring", methods=['GET', 'OPTIONS'])
def scoring():
    # check the score of the deployed model
    score = score_model()
    return f'F1 score: {str(score)}'

# Summary Statistics Endpoint


@app.route("/summarystats", methods=['GET', 'OPTIONS'])
def summarystats():
    # check means, medians, and modes for each column
    summary = dataframe_summary()
    return summary

# Diagnostics Endpoint


@app.route("/diagnostics", methods=['GET', 'OPTIONS'])
def diagnostics():
    # check timing and percent NA values
    nas = count_na()
    timing = execution_time()
    return f'Percentage of null values per column {nas}, Training timing: {timing[0]}, Ingestion timing: {timing[1]}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
