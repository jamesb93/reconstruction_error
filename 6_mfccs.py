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

## Paths
root = get_path()
audio_folder = os.path.join(root, 'DataAudio')
unique_audio_folder = os.path.join(root, 'DataAudioUnique')
unique_audio_files = ds_store(os.listdir(unique_audio_folder))
tmp = os.path.join(root, 'tmp')
## Hygiene
wipe_dir(tmp)

## Global Dicts for writing out results
mfcc_dict = mp.Manager().dict()

def analyse(idx):
    ## Setup paths/files etc
    mfcc_src = os.path.join(unique_audio_folder, unique_audio_files[idx])
    mfcc_features = os.path.join(tmp, f'{unique_audio_files[idx]}_features.wav')
    mfcc_stats = os.path.join(tmp, f'{unique_audio_files[idx]}_stats.wav' )
    ## Compute spectral shape descriptors
    subprocess.call(['mfcc', 
    '-source', mfcc_src, 
    '-features', mfcc_features, 
    '-fftsettings', '4096', '1024', '4096',
    '-numbands', '40',
    '-numcoeffs', '13',
    '-maxnumcoeffs', '13'])
    ## Now get the stats of the shape analysis
    subprocess.call(['stats', 
    '-source', mfcc_features, 
    '-stats', mfcc_stats,
    '-numderivs', '3'])
    ## Put Data in the global dictionary
    data = bufspill(mfcc_stats) ## Only grab the first seven values, we dont care about derivatives.
    ## This is going to have a column per MFCC with 14 values.
    try:
        data = data.flatten()
        list_data = data.tolist()
        mfcc_dict[unique_audio_files[idx]] = list_data
        ## Cleanup
        os.remove(mfcc_stats)
        os.remove(mfcc_features)
    except:
        print(f'There was no data to process for {mfcc_src}.')

def main():
    start = time.time()
    num_jobs = len(unique_audio_files)

    with mp.Pool() as pool:
        for i, _ in enumerate(
            pool.imap_unordered(analyse, range(num_jobs))
            , 1):
            sys.stderr.write('\rdone {0:%}'.format(i/num_jobs))

    end = time.time()
    json_out = os.path.join(root, 'mfcc.json')
    write_json(json_out, dict(mfcc_dict))
    time_taken = round(((end-start) / 60.), 2)
    print('\nProcess complete in:', time_taken)



    
