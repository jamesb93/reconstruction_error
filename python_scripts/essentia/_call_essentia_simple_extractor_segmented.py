import subprocess as sp
import multiprocessing as mp
import os
import sys 
import time
from datamosh.utils import check_make, wipe_dir
from datamosh.variables import unique_audio_folder, unique_audio_files, project_root, essentia_analysis


num_jobs = len(unique_audio_files)
simple_analysis_folder = os.path.join(essentia_analysis, 'simple_extractor_segmented')
check_make(simple_analysis_folder)
wipe_dir(simple_analysis_folder)

def process(idx):
    input_file = os.path.join(unique_audio_folder, unique_audio_files[idx])
    output_file = os.path.join(simple_analysis_folder, f'{unique_audio_files[idx]}.json')

    if not os.path.isfile(output_file):
        sp.call([
            'essentia_databend_simple_extractor', 
            input_file,
            output_file,
            '8192',
            '256',
        ])
    

with mp.Pool() as pool:
    for i, _ in enumerate(
        pool.imap_unordered(process, range(num_jobs))
        , 1):
        sys.stderr.write('\rdone {0:%}'.format(i/num_jobs))
