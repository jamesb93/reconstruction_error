import os
import subprocess
from shutil import copyfile
from databending_utilities import * # import all from the utilities script
import time
import numpy as np
from scipy.io import wavfile
import random
import time
import sys
from pydub import AudioSegment
import multiprocessing as mp
import audioread

## Paths
root = get_path()
audio_folder = os.path.join(root, 'DataAudio')
unique_audio_folder = os.path.join(root, 'DataAudioUnique')
unique_audio_files = ds_store(os.listdir(unique_audio_folder))
tmp = os.path.join(root, 'tmp')
## Hygiene
wipe_dir(tmp)

## Global Dicts for writing out results
sfm_dict = mp.Manager().dict()

def analyse(idx):
    ## Setup paths/files etc
    shape_src = os.path.join(unique_audio_folder, unique_audio_files[idx])
    shape_features = os.path.join(tmp, f'{unique_audio_files[idx]}_features.wav')
    shape_stats = os.path.join(tmp, f'{unique_audio_files[idx]}_stats.wav' )
    ## Compute spectral shape descriptors
    subprocess.call(['spectralshape', 
    '-source', shape_src, 
    '-features', shape_features, 
    '-fftsettings', '4096', '512', '4096'])
    ## Now get the stats of the shape analysis
    subprocess.call(['stats', 
    '-source', shape_features, 
    '-stats', shape_stats,
    '-numderivs', '1',
    '-startchan', '5',
    '-numchans', '1'])
    ## Put Data in the global dictionary
    data = bufspill(shape_stats)  ## Only grab the first seven values, we dont care about derivatives.
    try:
        sfm_dict[unique_audio_files[idx]] = data.tolist()
        os.remove(shape_stats)
        os.remove(shape_features)
    except:
        print(f'There was no data to process for {shape_src}.')
    
def main():
    start = time.time()
    num_jobs = len(unique_audio_files)
    with mp.Pool() as pool:
        for i, _ in enumerate(
            pool.imap_unordered(analyse, range(num_jobs))
            , 1):
            sys.stderr.write('\rdone {0:%}'.format(i/num_jobs))
    json_out = os.path.join(root, 'sfm.json')

    write_json(json_out, dict(sfm_dict))

    end = time.time()
    time_taken = round(((end-start) / 60.), 2)
    print('\nProcess complete in:', time_taken)


    
