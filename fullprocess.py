import json
import os
from scoring import score_model


with open('config.json', 'r') as f:
    config = json.load(f)
input_folder_path = config['input_folder_path']
prod_deployment_path = config['prod_deployment_path']
new_data_path = config['output_folder_path']

def go():
    # Check and read new data
    # read ingestedfiles.txt
    ingestedfiles = open(prod_deployment_path +'/ingestedfiles.txt', 'r')
    ingestedfiles = ingestedfiles.read().split(', ')

    # determine whether the source data folder has files that aren't listed in ingestedfiles.txt
    filenames = os.listdir(os.getcwd() + '/' + input_folder_path)
    
    new_files = []
    for each_filename in filenames:
        if ('.csv' in each_filename) & (each_filename not in ingestedfiles):
            new_files.append(each_filename)
        else: pass

    # Deciding whether to proceed, part 1
    if len(new_files) > 0:
        os.system('python ingestion.py')
        #Checking for model drift
        # load old model score
        prev_score = open(prod_deployment_path +'/latestscore.txt', 'r')
        
        # check the new score of the model
        new_score = score_model()
        
        # Deciding whether to proceed, part 2
        if float(new_score) > float(prev_score.read()):
            # Re-training
            os.system('python train.py')
            
            # Re-deployment
            os.system('python deployment.py')
        
            # Diagnostics and reporting
            os.system('python reporting.py')

            # starting flask app
            os.system('python app.py')
            
            # getting flask app endpoint responses
            os.system('python apicalls.py')
        else: pass

if __name__ == "__main__":
    go()
