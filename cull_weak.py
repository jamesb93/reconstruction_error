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

root = get_path()
unique_audio_folder = f'{root}/DataAudioUnique'
unique_audio_files = os.listdir(unique_audio_folder)
tmp = f'{root}/tmp'
loudness_json = f'{root}/unique_audio_loudness.json'
loudness_dict = dict()


def analyse(idx):
    src = f'{unique_audio_folder}/{unique_audio_files[idx]}'
    key = unique_audio_files[idx]
    # src = '/Users/jamesbradbury/desktop/browse.VC.db-wal.wav_242.wav'
    new_hash = random.getrandbits(128)
    loudness = f'{tmp}/loudness{new_hash}.wav'
    stats = f'{tmp}/stats{new_hash}.wav'
    subprocess.call(['loudness', '-source', src, '-features', loudness, '-windowsize', '17640', '-hopsize', '4410'])
    subprocess.call(['stats', '-source', loudness, '-stats', stats, '-numderivs', '1'])
    sr, data = wavfile.read(stats)
    loudness_dict[key] = data[0][0]
    os.remove(loudness)
    os.remove(stats)
    
    
start = time.time()
pool = mp.Pool() #use all available cores, otherwise specify the number you want as an argument
pool.map(analyse, range(len(unique_audio_files)))

## Dump as JSON
with open(loudness_json, 'w') as fp:
    json.dump(loudness_dict, fp, indent=4)
end = time.time()
time_taken = (end - start) / 60.
print('Loudness measurements complete.')
print('Completed in:', time_taken )
