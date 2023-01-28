import requests
import json
import os

#Specify a URL that resolves to your workspace
URL = "http://127.0.0.1:8000"

parameters = {
            "secret_key": "1652d576-484a-49fd-913a-6879acfa6ba4"
        }

# Load config.json and get path variables
with open('config.json', 'r') as f:
    config = json.load(f)
model_path = os.path.join(config['output_model_path'])

#Call each API endpoint and store the responses
response1 = requests.get(f"{URL}/prediction")
response2 = requests.get(f"{URL}/scoring")
response3 = requests.get(f"{URL}/summarystats")
response4 = requests.get(f"{URL}/diagnostics")

#combine all API responses
responses = [response1, response2, response3, response4]

#write the responses to your workspace
with open(model_path + '/apireturns.txt', 'w') as f:
    f.write(str(responses))


