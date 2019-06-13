import os
import subprocess
import multiprocessing as mp
import os
import json
from databending_utilities import *
import librosa
import numpy as np

root = get_path()
unique_audio_folder = f'{root}/DataAudioUnique'
unique_audio_files = os.listdir(unique_audio_folder)
tmp = f'{root}/tmp'


def analyse(idx):
    src = f'{unique_audio_folder}/{unique_audio_files[idx]}'
    # src = '/Users/jamesbradbury/desktop/browse.VC.db-wal.wav_242.wav'
    print(src)
    loudness = f'{tmp}/loudness.wav'
    stats = f'{tmp}/stats.wav'
    subprocess.call(['loudness', '-source', src, '-features', loudness, '-windowsize', '17640', '-hopsize', '4410'])
    subprocess.call(['stats', '-source', loudness, '-stats', stats, '-numderivs', '1'])
    y, sr = librosa.core.load(stats, sr=None)
    for sample in y:
        print(sample)
    # os.remove(loudness)
    # os.remove(stats)

analyse(0)
