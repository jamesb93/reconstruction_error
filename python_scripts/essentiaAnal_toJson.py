from databending_utilities import read_yaml, write_json, ds_store
from db_vars import root, parent, essentia_analysis

import os
import multiprocessing as mp
import sys

essentia_files = [x for x in ds_store(os.listdir(essentia_analysis))]

master_dict = mp.Manager().dict()

def extract(idx):
    file_name = essentia_files[idx]
    audio_name = os.path.splitext(file_name)[0]
    full_path = os.path.join(essentia_analysis, file_name)
    temp_yaml = read_yaml(full_path)
    del temp_yaml['metadata']
    master_dict[audio_name] = temp_yaml

num_jobs = len(essentia_files)
with mp.Pool() as pool:
    for i, _ in enumerate(
            pool.imap_unordered(extract, range(num_jobs)), 1):
        print(i)

analysis_out = os.path.join(parent, 'analysis_data', 'essentia_analysis.json')
write_json(analysis_out, dict(master_dict))
    

