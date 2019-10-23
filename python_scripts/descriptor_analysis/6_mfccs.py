import os
import sys
import time
import subprocess
import multiprocessing as mp
import tempfile
from shutil import copyfile
from datamosh.utils import bufspill, write_json
from datamosh.variables import unique_audio_files, unique_audio_folder

# You need to pass in the input directory and the output file
if len(sys.argv) < 2:
    print('You need to pass an output file.')
    exit()

this_script = os.path.dirname(os.path.realpath(__file__))

output_file = sys.argv[1]
output_json = os.path.join(this_script, output_file)

# temporary directory for files
tmp_dir = tempfile.mkdtemp()

## Global Dicts for writing out results
mfcc_dict = mp.Manager().dict()

def analyse(idx):
    # Setup paths/files etc
    mfcc_src = os.path.join(unique_audio_folder, unique_audio_files[idx])
    mfcc_features = os.path.join(tmp_dir, f'{unique_audio_files[idx]}_features.wav')
    mfcc_stats = os.path.join(tmp_dir, f'{unique_audio_files[idx]}_stats.wav' )
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

num_jobs = len(unique_audio_files)

with mp.Pool() as pool:
    for i, _ in enumerate(
        pool.imap_unordered(analyse, range(num_jobs)), 1):
            sys.stderr.write('\rAnalysis Progress {0:%}'.format(i/num_jobs))

write_json(json_out, dict(mfcc_dict))
os.rmdir(tmp_dir)