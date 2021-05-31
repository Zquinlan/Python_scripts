import requests
import json
import pandas as pd
import numpy as np
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('jobID', help="This is the task number of your GNPS job which can be found in the url of your GNPS job")
parser.add_argument('jobType', help= "The type of job options are 'canopus', 'library', 'analog', 'csiFingerID', 'edges'")
args = parser.parse_args()

jobID = args.jobID
jobType = args.jobType

if jobType == 'canopus':
    url = str('https://gnps.ucsd.edu/ProteoSAFe/result_json.jsp?task=' + jobID + '&view=canopus_summary') 
if jobType == 'library':
    url = str('https://gnps.ucsd.edu/ProteoSAFe/result_json.jsp?task=' + jobID + '&view=view_all_annotations_DB')
if jobType == 'analog':
    url = str('https://gnps.ucsd.edu/ProteoSAFe/result_json.jsp?task=' + jobID + '&view=view_all_analog_annotations_DB')
# if jobType == 'network': #Fix this one
#     url = str('https://gnps.ucsd.edu/ProteoSAFe/result_json.jsp?task=' + jobID + '&view=clusterinfo_summary')
if jobType == 'csiFingerID':
    url = str('https://gnps.ucsd.edu/ProteoSAFe/result_json.jsp?task=' + jobID + '&view=compound_identifications_summary')
if jobType == 'edges':
    url = str('https://gnps.ucsd.edu/ProteoSAFe/result_json.jsp?task=' + jobID + '&view=network_pairs_specnets_allcomponents')

# request JSON files from GNPS, clean and load into pandas
request = requests.get(url) # Download JSON from GNPS
clean = request.text.replace('{ "blockData" : [', '[').replace('] }', ']').strip()
df = pd.read_json(clean)

df.to_csv(str(jobType + '.csv'))