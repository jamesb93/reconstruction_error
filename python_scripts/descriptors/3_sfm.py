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
sfm_dict = mp.Manager().dict()

def analyse(idx: int):
    ## Setup paths/files etc
    shape_src = os.path.join(unique_audio_folder, unique_audio_files[idx])
    shape_features = os.path.join(tmp_dir, f'{unique_audio_files[idx]}_features.wav')
    shape_stats = os.path.join(tmp_dir, f'{unique_audio_files[idx]}_stats.wav' )
    ## Compute spectral shape descriptors
    subprocess.call([
    'fluid-spectralshape', 
    '-source', shape_src, 
    '-features', shape_features, 
    '-fftsettings', '4096', '512', '4096'])
    ## Now get the stats of the shape analysis
    subprocess.call([
    'fluid-stats', 
    '-source', shape_features, 
    '-stats', shape_stats,
    '-numderivs', '1',
    '-startchan', '5',
    '-numchans', '1'])
    ## Put Data in the global dictionary
    data = bufspill(shape_stats)  ## Only grab the first seven values, we dont care about derivatives.
    try:
        sfm_dict[unique_audio_files[idx]] = data.tolist()
        os.remove(shape_stats)
        os.remove(shape_features)
    except:
        print(f'There was no data to process for {shape_src}.')
    
start = time.time()
num_jobs = len(unique_audio_files)
with mp.Pool() as pool:
    for i, _ in enumerate(
        pool.imap_unordered(analyse, range(num_jobs))
        , 1):
        sys.stderr.write('\rAnalysis Progress {0:%}'.format(i/num_jobs))

write_json(output_json, dict(sfm_dict))
os.rmdir(tmp_dir)
end = time.time()
time_taken = round(((end-start) / 60.), 2)
print('\nProcess complete in:', time_taken)