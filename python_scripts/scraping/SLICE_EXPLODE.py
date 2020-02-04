import os
import sys
import time
import tempfile
import argparse
import subprocess
import numpy as np
import multiprocessing as mp
from shutil import copyfile
from pydub import AudioSegment
from datamosh.utils import samps2ms, check_make, bufspill # import all from the utilities script

parser = argparse.ArgumentParser(description='Slice a folder of audio files using fluid-noveltyslice.')
parser.add_argument('-i', '--infolder', type=str, help='The input folder to slice')
parser.add_argument('-o', '--outfolder', type=str, help='The output folder for sliced audio')
args = parser.parse_args()

if not args.outfolder or not args.infolder:
    print('Please provide a valid input/output folder!')
    exit()

# Prepare for work
tmp_dir = tempfile.mkdtemp()
input_folder = args.infolder
input_files = os.listdir(input_folder)
output_folder = args.outfolder
check_make(output_folder)

def explode(idx: int):
    ## NoveltySlice on File
    novelty_src = os.path.join(input_folder, input_files[idx])
    novelty_indices = os.path.join(tmp_dir, f'{input_files[idx]}_slices.wav')
    subprocess.call([
        'fluid-noveltyslice', 
        '-source', novelty_src, 
        '-indices', novelty_indices, 
        '-fftsettings', '2048', '1024', '2048', 
        '-threshold', '0.61', 
        '-kernelsize', '3', 
        '-filtersize', '1'
    ])
    # Turn slices wav into a list
    data = bufspill(novelty_indices)
    sound = bufspill(novelty_src)
    book_end = len(sound) # We get the length of the buffer and keep this for later
    t_audio = AudioSegment.from_wav(novelty_src)
    no_ext = os.path.basename(novelty_src)
    no_ext = os.path.splitext(no_ext)[0]
    data = np.append(data, book_end) # Append the length of the original sound file to our slices to create a boundary
    # Explode to individual files
    for i in range(len(data) - 1):
        start = samps2ms(data[i], 44100)
        end   = samps2ms(data[i+1], 44100)
        t_output = t_audio[start:end]
        t_output.export(os.path.join(output_folder, f'{no_ext}_{i}.wav'), format='wav')
    os.remove(novelty_indices)

# Start process workers
start = time.time()
num_jobs = len(input_files)
with mp.Pool() as pool:
    for i, _ in enumerate(
        pool.imap_unordered(explode, range(num_jobs))
        , 1):
        sys.stderr.write('\rSlicing process {0:%}'.format(i/num_jobs))

end = time.time()
time_taken = round(((end-start) / 60.), 2)
print('\nProcess complete in:', time_taken)