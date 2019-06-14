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


root = get_path()
audio_folder = os.path.join(root, 'DataAudio')
unique_audio_folder = os.path.join(root, 'DataAudioUnique')
audio_files = os.listdir(audio_folder)
audio_files = ds_store(audio_files)
tmp = os.path.join(root, 'tmp')

wipe_dir(unique_audio_folder)
wipe_dir(tmp)
def explode(idx):
    ## NoveltySlice on File
    novelty_src = os.path.join(audio_folder, audio_files[idx])
    novelty_indices = os.path.join(tmp, f'{audio_files[idx]}_slices.wav')
    subprocess.call(['rtnoveltyslice', '-source', novelty_src, '-indices', novelty_indices, '-fftsettings', '2048', '1024', '2048', '-threshold', '0.61', '-kernelsize', '3', '-filtersize', '1'])
    ## Turn slices wav into a list
    try:
        sr, data = wavfile.read(novelty_indices)
    except FileNotFoundError:
        print(f'I was not able to find the file: {novelty_indices}')
    
    t_audio = AudioSegment.from_wav(novelty_src)
    no_ext = os.path.basename(novelty_src)
    no_ext = os.path.splitext(no_ext)[0]
    
    ## Explode to individual files
    for i in range(len(data) - 1):
        start = samps2ms(data[i], 44100)
        end   = samps2ms(data[i+1], 44100)
        t_output = t_audio[start:end]
        t_output.export(os.path.join(unique_audio_folder, f'{no_ext}_{i}.wav'), format='wav')
    os.remove(novelty_indices)
start = time.time()
num_jobs = len(audio_files)
with mp.Pool() as pool:
    for i, _ in enumerate(
        pool.imap_unordered(explode, range(num_jobs))
        , 1):
        sys.stderr.write('\rdone {0:%}'.format(i/num_jobs))

end = time.time()
time_taken = round(((end-start) / 60.), 2)
print('Process complete in:', time_taken)


    
