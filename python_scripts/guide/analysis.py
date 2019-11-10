import os
import sys
import time
import tempfile
import argparse
import subprocess
import multiprocessing as mp
from shutil import copyfile, rmtree
from datamosh.utils import bufspill, write_json, printp
from datamosh.variables import audio_files, audio_folder, analysis_data

parser = argparse.ArgumentParser(description='Analyse all audio files with a shifting window.')
parser.add_argument('-i', '--infolder', type=str, help='The input folder to analyse')
parser.add_argument('-o', '--outfile', type=str, help='The output JSON containing analysis')
args = parser.parse_args()

# You need to pass in the input directory and the output file
if not args.infolder or not args.outfile:
    print('You need to provide an input folder/output file.')
    exit()

this_script = os.path.dirname(os.path.realpath(__file__))

# Prepare for work
tmp_dir = tempfile.mkdtemp()
input_folder = args.infolder
input_files = os.listdir(input_folder)
output_json = os.path.join(analysis_data, args.outfile)

# Global Dicts for writing out results
mfcc_dict = mp.Manager().dict()

def analyse(idx):
    # Setup paths/files etc
    mfcc_src        = os.path.join(input_folder, input_files[idx])
    # Compute spectral shape descriptors
    subprocess.call([
        'fluid-mfcc', 
        '-source', mfcc_src, 
        '-features', mfcc_features, 
        '-fftsettings', '8192', '256', '8192',
        '-numbands', '40',
        '-numcoeffs', '13',
        '-maxnumcoeffs', '13'
    ])
    # Now get the stats of the shape analysis
    subprocess.call([
        'fluid-stats', 
        '-source', mfcc_features, 
        '-stats', mfcc_stats,
        '-numderivs', '3'
    ])
    data = bufspill(mfcc_stats)
    try:
        data = data.flatten()
        list_data = data.tolist()
        mfcc_dict[unique_audio_files[idx]] = list_data
    except:
        print(f'There was no data to process for {mfcc_src}.')

num_jobs = len(input_files)

with mp.Pool() as pool:
    for i, _ in enumerate(
        pool.imap_unordered(analyse, range(num_jobs)), 1):
            sys.stderr.write('\rAnalysis Progress {0:%}'.format(i/num_jobs))

write_json(output_json, dict(mfcc_dict))
rmtree(tmp_dir)
printp('Finished analysis')