########## Segment all files in /DataAudio and return a folder full of segments in the format $file_$segmentnumber.wav and $file_slices.wav ##########
import os
import subprocess
from shutil import copyfile
from databending_utilities import * # import all from the utilities script
import time

root = get_path()
audio_folder = os.path.join(root, 'DataAudio')
slices_folder = os.path.join(root, 'DataSlices')
audio_files = os.listdir(audio_folder)
slices_files = os.listdir(slices_folder)

### Make a list sorted by size ###
audio_files_fp = []
for item in audio_files:
    audio_files_fp.append(os.path.join(audio_folder, item))

sorted_audio_files = sorted(audio_files_fp, key=os.path.getsize)

overwrite = 1 ## Overwrite mode. If 1 then all existing analysis is overwritten. If 0, check if exists first.
start = time.time()

for raw_audio in sorted_audio_files:

    no_ext = os.path.basename(raw_audio)
    no_ext = os.path.splitext(no_ext)[0]

    out = f'{slices_folder}/{no_ext}_slices.wav'

    print('Progress')
    print('Segmenting:', raw_audio)
    progress += 1
    src = raw_audio
    indices = out

    ### No overwrite ###
    if overwrite == 0:
        if not os.path.isfile(out):
            process = subprocess.Popen(['noveltyslice', '-source', src, '-indices', indices, '-fftsettings', '2048', '-1', '-1', '-threshold', '0.8', '-kernelsize', '3'])
            process.wait()
            print('Finished segmenting:', raw_audio)
        else:
            print('Found existing analysis for:', raw_audio)
    
    ### Overwrite ###
    elif overwrite == 1:
        process = subprocess.Popen(['noveltyslice', '-source', src, '-indices', indices, '-fftsettings', '2048', '-1', '-1', '-threshold', '0.8', '-kernelsize', '3'])
        process.wait()
        print('Finished segmenting:', raw_audio)

end = time.time()
print('Process took:', (end-start))
    





saf