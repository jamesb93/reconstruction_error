from databending_utilities import samps2ms, wipe_dir, read_json, write_json, norm_np, read_yaml, ds_store, printp
import os
import json
from sklearn.preprocessing import StandardScaler
from sklearn import manifold
import numpy as np
from db_vars import root, parent, essentia_analysis
import multiprocessing as mp
import sys
import numpy as np

def convert_nan(vec):
    for i in range(len(vec)):
        if vec[i] == "nan" or vec[i] == "inf":
            vec[i] = np.float(0.0)
    return vec

def extract(idx):
    features = read_yaml(os.path.join(parent, essentia_analysis, file_list[idx]))
    audio_file_name = file_list[idx]
    audio_file_name = audio_file_name[:-5]
    temp = []
    for key in features:
        if key != 'metadata' and key != 'dynamicComplexity' and key != 'loudness':
            for stat in features[key]:
                if type(features[key][stat]) == list:
                    [temp.append(x) for x in features[key][stat]]
                else:
                    temp.append(features[key][stat])
        elif key == 'dynamicComplexity' or key == 'loudness':
           temp.append(features[key])
    
    raw_data[audio_file_name] = temp


file_list = ds_store(os.listdir(essentia_analysis))
num_jobs = len(file_list)
raw_data = {}

printp('Concatenating Data for Reduction')
for i in range(num_jobs):
    extract(i)

printp('Finished Raw Data Concatenation')

output_file = os.path.join(parent, 'analysis_data', 'essentia_cat.json')
write_json(output_file, raw_data)
