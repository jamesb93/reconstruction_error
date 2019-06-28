import os
from databending_utilities import get_path
import shutil

root = get_path()

nmf_folder = os.path.join(root, 'DataAudioNMF')
nmf_files = os.listdir(nmf_folder)
three_chan_folder = os.path.join(root, 'DataAudioNMF_3')

for file in nmf_files:
    basename = os.path.splitext(file)[0]
    if basename[-1:] == '3':
        shutil.move(os.path.join(nmf_folder, file), os.path.join(three_chan_folder, file))


    