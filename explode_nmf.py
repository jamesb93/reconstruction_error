import os
import multiprocessing as mp
import subprocess as sp
from databending_utilities import get_path
import time
import sys
from pydub import AudioSegment

root = get_path()

nmf_folder = os.path.join(root, 'DataAudioNMF_2')
nmf_files = os.listdir(nmf_folder)
explode_folder = os.path.join(root, 'DataAudioNMF_2_Explode')

def explode(idx):
    no_ext = os.path.splitext(nmf_files[idx])[0]
    input_file = os.path.join(nmf_folder, nmf_files[idx])

    ## out strings
    left_file_out  = os.path.join(root, 'DataAudioNMF_2_Explode', f'{no_ext}_L.wav')
    right_file_out = os.path.join(root, 'DataAudioNMF_2_Explode', f'{no_ext}_R.wav')

    sp.call([
        'ffmpeg',
        '-i',
        input_file,
        '-map_channel',
        '0.0.0',
        left_file_out
    ])

    sp.call([
        'ffmpeg',
        '-i',
        input_file,
        '-map_channel',
        '0.0.1',
        right_file_out
    ])


num_jobs = len(nmf_files)
for i in range(num_jobs):
    explode(i)
# with mp.Pool() as pool:
#     for i, _ in enumerate(
#         pool.imap_unordered(explode, range(num_jobs))
#         , 1):
#         sys.stderr.write('\rdone {0:%}'.format(i/num_jobs))
