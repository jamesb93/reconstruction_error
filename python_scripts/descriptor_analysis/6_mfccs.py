import sys
sys.path.append('../')
import os
import subprocess
import multiprocessing as mp
import numpy as np
import random
import time
from scipy.io import wavfile
from shutil import copyfile
from datamosh.utils import get_path, read_json, write_json, ds_store, wipe_dir, bufspill # import all from the utilities script
from datamosh.variables import root, audio_folder, unique_audio_files, unique_audio_folder, tmp

this_script = os.getcwd()

def analyse(idx):
    ## Setup paths/files etc
    mfcc_src = os.path.join(unique_audio_folder, unique_audio_files[idx])
    mfcc_features = os.path.join(tmp, f'{unique_audio_files[idx]}_features.wav')
    mfcc_stats = os.path.join(tmp, f'{unique_audio_files[idx]}_stats.wav' )
    ## Compute spectral shape descriptors
    subprocess.call([
        'mfcc', 
        '-source', str(mfcc_src), 
        '-features', str(mfcc_features), 
        '-fftsettings', '8192', '256', '8192',
        '-numbands', '40',
        '-numcoeffs', '13',
        '-maxnumcoeffs', '13'])
    ## Now get the stats of the shape analysis
    subprocess.call([
        'stats', 
        '-source', str(mfcc_features), 
        '-stats', str(mfcc_stats),
        '-numderivs', '3'])
    data = bufspill(mfcc_stats)
    try:
        data = data.flatten()
        list_data = data.tolist()
        mfcc_dict[unique_audio_files[idx]] = list_data
    except:
        print(f'There was no data to process for {mfcc_src}.')

def process():
    num_jobs = len(unique_audio_files)

    with mp.Pool() as pool:
        for i, _ in enumerate(
            pool.imap_unordered(analyse, range(num_jobs)), 1):
                sys.stderr.write('\rdone {0:%}'.format(i/num_jobs))



if __name__ == '__main__':
    wipe_dir(tmp)
    ## Global Dicts for writing out results
    mfcc_dict = mp.Manager().dict()
    process()
    json_out = os.path.join(this_script, 'mfcc.json')
    write_json(json_out, dict(mfcc_dict))
    

    
