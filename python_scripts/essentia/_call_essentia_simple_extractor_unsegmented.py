import subprocess as sp
import multiprocessing as mp
import os
import sys 
import time
from datamosh.utils import check_make
from datamosh.variables import audio_folder, audio_files, project_root, essentia_analysis


num_jobs = len(audio_files)
output_folder = os.path.join(essentia_analysis, 'simple_extractor_unsegmented')
check_make(output_folder)

def process(idx):
    input_file = os.path.join(audio_folder, audio_files[idx])
    output_file = os.path.join(output_folder, f'{audio_files[idx]}.json')

    if not os.path.isfile(output_file):
        sp.call([
            'essentia_databend_simple_extractor', 
            input_file,
            output_file,
            '4096',
            '1024'
        ])
    

with mp.Pool() as pool:
    for i, _ in enumerate(
        pool.imap_unordered(process, range(num_jobs))
        , 1):
        sys.stderr.write('\rdone {0:%}'.format(i/num_jobs))
