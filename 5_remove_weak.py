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
import simpleaudio as sa

root = get_path()
def update_dictionaries(*arg):
    '''
    Takes a list of bad entries and any number of json files. It updates the jsons by removing bad entries.
    '''
    for json in arg:
        t_dict = read_json(os.path.join(root, json))
        for bad_entry in undesirables:
            del t_dict[bad_entry]
        write_json(os.path.join(root, json), t_dict)

undesirables = []

## Audio files
unique_audio_folder = os.path.join(root, 'DataAudioUnique')
unique_audio_files = os.listdir(unique_audio_folder)
unique_audio_files = ds_store(unique_audio_files)
tmp = os.path.join(root, 'tmp')

## Load json's for querying
loudness_json = read_json(os.path.join(root, 'loudness.json'))
sfm_json = read_json(os.path.join(root, 'sfm.json'))
mfcc_json = read_json(os.path.join(root, 'mfcc.json'))

for key in loudness_json:
    values = loudness_json[key]
    t_min = values[0]
    t_max = values[1]
    t_median = values[2]
    thresh = -150
    if t_median < thresh:
        print(f'{key}: {values}\n')
        wave_obj = sa.WaveObject.from_wave_file(os.path.join(unique_audio_folder, key))
        play_obj = wave_obj.play()
        play_obj.wait_done()

# user_input = input("1 to delete, 0 to pass. \n")
user_input = 0

if user_input == 1:
    update_dictionaries('mfcc.json', 'sfm.json', 'loudness.json')
elif user_input == 0:
    print('Did not edit anything.')
