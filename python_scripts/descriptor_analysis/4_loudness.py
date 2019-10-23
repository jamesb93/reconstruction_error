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

loudness_dict = mp.Manager().dict()

def analyse(idx):

    key = unique_audio_files[idx]
    src = os.path.join(unique_audio_folder, key)
    loudness = os.path.join(tmp_dir, f'loudness_{key}.wav')
    stats = os.path.join(tmp_dir, f'stats_{key}.wav')
    subprocess.call([
        'fluid-loudness', 
        '-source', src, 
        '-features', loudness, 
        '-windowsize', '17640', 
        '-hopsize', '4410'
    ])

    subprocess.call([
        'fluid-stats', 
        '-source', loudness, 
        '-stats', stats, 
        '-numderivs', '0'
    ])

    data = bufspill(stats)[0]
    t_min = data[4]
    t_max = data[6]
    t_median = data[5]
    loudness_dict[key] = [t_min, t_max, t_median]
    os.remove(loudness)
    os.remove(stats)


start = time.time()
num_jobs = len(unique_audio_files)
with mp.Pool() as pool:
    for i, _ in enumerate(
        pool.imap_unordered(analyse, range(num_jobs))
        , 1):
        sys.stderr.write('\rAnalysis Progress {0:%}'.format(i/num_jobs))
    

write_json(output_json, dict(loudness_dict) )
os.rmdir(tmp_dir)
end = time.time()
time_taken = (end - start) / 60.
print('\nProcess complete in:', time_taken)
