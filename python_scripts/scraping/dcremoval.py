import subprocess as sp
import os
import sys
import multiprocessing as mp
from datamosh.variables import unique_audio_folder, unique_audio_files, project_root
from datamosh.utils import check_make


filtered_folder = os.path.join(project_root, 'DataAudioUnique_DC')
check_make(filtered_folder)
num_jobs = len(unique_audio_files)

def remove_dc(infile: str, outfile: str, hertz: int):
    sp.Popen([
        'sox',
        '-D',
        '-V0',
        infile,
        outfile,
        'highpass',
        hertz,
    ])
def process(idx: int):
        remove_dc(
            os.path.join(unique_audio_folder, unique_audio_files[idx]),
            os.path.join(filtered_folder, unique_audio_files[idx]),
            '10'
        )

with mp.Pool() as pool:
    for i, _ in enumerate(
        pool.imap_unordered(process, range(num_jobs))
        , 1):
        sys.stderr.write('\rdone {0:%}'.format(i/num_jobs))
    