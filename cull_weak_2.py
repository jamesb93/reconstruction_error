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

with open(loudness_json) as json_file:
    data = json.load(json_file)
counter = 0
for key in data:
    value = data[key]
    if value < -24.0:
        counter += 1
        print(f'{key}: {value}')

print(counter)
    


