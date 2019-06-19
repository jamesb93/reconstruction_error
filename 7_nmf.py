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
try:
    import cPickle as pickle
except ImportError:  # python 3.x
    import pickle

## Paths
root = get_path()
audio_folder = os.path.join(root, 'DataAudio')
unique_audio_folder = os.path.join(root, 'DataAudioUnique')
unique_audio_files = os.listdir(unique_audio_folder)
tmp = os.path.join(root, 'tmp')
## Hygiene
wipe_dir(tmp)
wipe_dir(os.path.join(root, 'DataAudioNMF'))

components_map = ['2', '3']

def analyse(idx):
    for components in components_map:
        ## Setup paths/files etc
        nmf_src = os.path.join(unique_audio_folder, unique_audio_files[idx])
        nmf_out = os.path.join(tmp, f'{unique_audio_files[idx]}-C{components}-NMF.wav')
        ## Compute spectral shape descriptors
        subprocess.call([
            'nmf', 
            '-source', nmf_src, 
            '-resynth', nmf_out, 
            '-fftsettings', '2048', '1024', '2048',
            '-components', str(components),
            '-iterations', '25'])

def main():
    start = time.time()
    num_jobs = len(unique_audio_files)

    with mp.Pool() as pool:
        for i, _ in enumerate(
            pool.imap_unordered(analyse, range(num_jobs))
            , 1):
            sys.stderr.write('\rdone {0:%}'.format(i/num_jobs))

    end = time.time()
    time_taken = round(((end-start) / 60.), 2)
    print('\nProcess complete in:', time_taken)

main()


    
