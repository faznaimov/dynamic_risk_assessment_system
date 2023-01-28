# Dynamic Risk Assessment System


- Project **Dynamic Risk Assessment System** in [ML DevOps Engineer Nanodegree](https://www.udacity.com/course/machine-learning-dev-ops-engineer-nanodegree--nd0821) program by Udacity.

## Table of Contents

- [Introduction](#dynamic-risk-assessment-system)
- [Project Description](#project-description)
- [Files and Data Description](#files-and-data-description)
- [Usage](#usage)
  * [Create Environment](#create-environment)
  * [Run The App on Local Machine](#run-the-app-on-local-machine)
  * [Set Up Cronjob](#set-up-cronjob)
  * [Run New Data Check and Model Drift Manually](#run-new-data-check-and-model-drift-manually)
- [License](#license)

## Project Description
Project to create, deploy, and monitor a risk assessment ML model that will estimate the attrition risk of each of the company's 10,000 clients. Project covers 4 aspects of MLOps:
1. New data detection and ingestion
2. Training, scoring, and deploying ML model
3. Model diagnostics
4. Model reporting

[Deployed App](https://dynamic-risk-assesment.onrender.com)

## App screenshot

![App](/images/app.png)

## Files and Data description
The directories structure are list as below:
```bash
.
├── ingesteddata
│   └── finadata.csv
├── models
│   ├── apireturns.txt
│   ├── confusionmatrix.png
│   ├── latestscore.txt
│   └── trainedmodel.pkl
├── screenshots
│   └── app.png
├── production_deployment
│   ├── ingestedfiles.txt
│   ├── latestscore.txt
│   └── trainedmodel.pkl
├── sourcedata
│   ├── dataset3.csv
│   └── dataset4.csv
├── templates
│   └── index.html
├── testdata
│   └── testdata.csv
├── apicalls.py
├── app.py
├── config.json
├── cronjob.txt
├── deployment.py
├── diagnostics.py
├── LICENSE
├── README.md
├── reporting.py
├── requirements.txt
├── scoring.py
├── test.py
├── training.py
└── wsgi.py
```

- ```training.py```: Python script meant to train an ML model
- ```scoring.py```: Python script meant to score an ML model
- ```deployment.py```: Python script meant to deploy a trained ML model
- ```ingestion.py```: Python script meant to ingest new data
- ```diagnostics.py```: Python script meant to measure model and data diagnostics
- ```reporting.py```: Python script meant to generate reports about model metrics
- ```app.py```: Python script meant to contain API endpoints
- ```wsgi.py```: Python script to help with API deployment
- ```apicalls.py```: Python script meant to call your API endpoints
- ```fullprocess.py```: script meant to determine whether a model needs to be re-deployed, and to call all other Python scripts when needed
- ```cronjob.txt```: crontab text runs the fullprocess.py script every 10 min

fullprocess.py logic:
![Full Process](/images/fullprocess.jpg)

## Usage

### Create Environment
Make sure to have conda installed and ready.

```bash
> conda create -n [envname] python=3.8
> pip install -r requirements.txt
```

### Run The App on Local Machine
```
> python app.py
```

### Set Up Cronjob
```
> service cron start
> crontab -e
Press the "i" key
Insert a cron job from cronjob.txt
Press the escape key
Type ":wq"
```

### Run New Data Check and Model Drift Manually
```
> python fullprocess.py
```

## License

[License](LICENSE)
