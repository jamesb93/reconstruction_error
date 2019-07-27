import os
import subprocess
import multiprocessing as mp
import os
import json
from databending_utilities import *
import numpy as np
from scipy.io import wavfile
import random
import time
import sys
from db_vars import root, unique_audio_files, unique_audio_folder, tmp

loudness_json = os.path.join(root, 'loudness.json')
loudness_dict = mp.Manager().dict()

def analyse(idx):
    src = f'{unique_audio_folder}/{unique_audio_files[idx]}'
    key = unique_audio_files[idx]
    loudness = f'{tmp}/loudness{key}.wav'
    stats = f'{tmp}/stats{key}.wav'
    subprocess.call(['loudness', '-source', src, '-features', loudness, '-windowsize', '17640', '-hopsize', '4410'])
    subprocess.call(['stats', '-source', loudness, '-stats', stats, '-numderivs', '1'])
    try:
        data = bufspill(stats)[0][:7]
        t_min = data[4]
        t_max = data[6]
        t_median = data[5]
        loudness_dict[key] = [t_min, t_max, t_median]
        os.remove(loudness)
        os.remove(stats)
    except:
        print(f'There was no data to process for {src}.')

def main():
    start = time.time()
    num_jobs = len(unique_audio_files)
    with mp.Pool() as pool:
        for i, _ in enumerate(
            pool.imap_unordered(analyse, range(num_jobs))
            , 1):
            sys.stderr.write('\rdone {0:%}'.format(i/num_jobs))
        

    write_json(loudness_json, dict(loudness_dict) )

    end = time.time()
    time_taken = (end - start) / 60.
    print('\nProcess complete in:', time_taken)
