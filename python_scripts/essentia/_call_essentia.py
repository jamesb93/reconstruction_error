import subprocess as sp
import multiprocessing as mp
import os
import sys 
import time
from db_vars import unique_audio_folder, unique_audio_files, tmp


num_jobs = len(unique_audio_files)

def process(idx):

    input_file = os.path.join(unique_audio_folder, unique_audio_files[idx])
    output_file = os.path.join(tmp, f'{unique_audio_files[idx]}.yaml')

    if not os.path.isfile(output_file):
        sp.call([
            'essentia_streaming_batchanal', 
            input_file,
            output_file
        ])
    

with mp.Pool() as pool:
    for i, _ in enumerate(
        pool.imap_unordered(process, range(num_jobs))
        , 1):
        sys.stderr.write('\rdone {0:%}'.format(i/num_jobs))
