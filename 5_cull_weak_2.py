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
unique_audio_folder = f'{root}/DataAudioUnique'
unique_audio_files = os.listdir(unique_audio_folder)
unique_audio_files.remove('.DS_Store')

tmp = os.path.join(root, 'tmp')
loudness_json = os.path.join(root, 'unique_audio_loudness.json')

with open(loudness_json) as json_file:
    data = json.load(json_file)

counter = 0
for key in data:
    value = data[key]
    if value < -50:
        counter += 1
        wave_obj = sa.WaveObject.from_wave_file(os.path.join(unique_audio_folder, key))
        play_obj = wave_obj.play()
        play_obj.wait_done()
#         print(f'{key}: {value}')

## Removing stuff
# for key in data:
#     value = data[key]
#     if value < -60:
#         os.remove(os.path.join(unique_audio_folder, key))
#         data.pop(key, None)
#         ## write dict back out
# with open(loudness_json) as json_file:
#     json.dump(data, json_file)
    


