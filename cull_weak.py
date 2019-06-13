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

root = get_path()
unique_audio_folder = f'{root}/DataAudioUnique'
unique_audio_files = os.listdir(unique_audio_folder)
unique_audio_files.remove('.DS_Store')
tmp = f'{root}/tmp'
loudness_json = f'{root}/unique_audio_loudness.json'

loudness_dict = mp.Manager().dict()

def analyse(idx):
    src = f'{unique_audio_folder}/{unique_audio_files[idx]}'
    key = unique_audio_files[idx]
    loudness = f'{tmp}/loudness{key}.wav'
    stats = f'{tmp}/stats{key}.wav'
    subprocess.call(['loudness', '-source', src, '-features', loudness, '-windowsize', '17640', '-hopsize', '4410'])
    subprocess.call(['stats', '-source', loudness, '-stats', stats, '-numderivs', '1'])
    try:
        sr, data = wavfile.read(stats)
    except FileNotFoundError:
        print(f'I was not able to find the file: {key}')
    # loudness_dict[key] = data[0][0]
    loudness_dict[key] = float(data[0][0])
    os.remove(loudness)
    os.remove(stats)

start = time.time()
pool = mp.Pool() #use all available cores, otherwise specify the number you want as an argument
num_jobs = len(unique_audio_files)
for i, _ in enumerate(
    pool.imap_unordered(analyse, range(num_jobs))
    , 1):
    sys.stderr.write('\rdone {0:%}'.format(i/num_jobs))
        
output_dict = dict(loudness_dict)

with open(loudness_json, 'w') as fp:
    json.dump(output_dict, fp, indent=4)

end = time.time()
time_taken = (end - start) / 60.
print('Loudness measurements complete.')
print('Completed in:', time_taken )
