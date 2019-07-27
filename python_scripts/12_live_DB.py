###
# Exploring the Live_DB_34.wav data-audio.
###
import numpy as np
import os
import subprocess as sub
from databending_utilities import read_json, write_json, bufspill, list_to_coll
from db_vars import root, unique_audio_files, unique_audio_folder, tmp
np.set_printoptions(suppress=True)

list_of_files = os.path.join(root, 'Live-files-34.db.txt')
f = open(list_of_files, 'w+')
live_db_anal = {}

for file in unique_audio_files:
    if 'Live-files-34.db_' in file:
        loudness_src = os.path.join(unique_audio_folder, file)
        loudness_features = os.path.join(tmp, file)
        # Loudness
        sub.call([
            'loudness',
            '-source', loudness_src,
            '-features', loudness_features,
            '-windowsize', '17640',
            '-hopsize', '4410'])
        # Stats
        loudness_stats = os.path.join(tmp, f'{file}_stats.wav')
        sub.call([
            'stats',
            '-source', loudness_features,
            '-stats', loudness_stats,
            '-numderivs', '1'])
        
        data = bufspill(loudness_stats)[0][6]
        live_db_anal[file] = data

json_out_file = os.path.join(root, 'live_db_analysis.json')
write_json(json_out_file, live_db_anal)

## Make a coll of the file names
names = [k for k in live_db_anal.keys()]
list_to_coll(names, os.path.join(root, 'live-db-list.txt'))
        
