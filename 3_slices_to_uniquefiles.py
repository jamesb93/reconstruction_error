from pydub import AudioSegment
from databending_utilities import get_path, samps2ms, wipe_dir
import os
import json
import multiprocessing
import time
start = time.time()

def explode(idx):
    entry = data[idx][0]
    slice_list = data[idx][1]
    slice_list = slice_list[1:]
    t_file = AudioSegment.from_wav(f'{audio_folder}/{entry}')
    print('Slicing:', entry)
    
    for i in range(len(slice_list) - 1):
        slice_num = i
        start = samps2ms(slice_list[i],   44100)
        end   = samps2ms(slice_list[i+1], 44100)
        t_output = t_file[start:end]
        t_output.export(f'{output_folder}/{entry}_{slice_num}.wav', format='wav')

root = get_path()
audio_folder = f'{root}/DataAudio'
audio_files = os.listdir(audio_folder)
output_folder = f'{root}/DataAudioUnique'
slices_json = f'{root}/audio_slices.json'

wipe_dir(output_folder)
with open(slices_json) as f:
    slice_data = json.load(f)

data = list(slice_data.items()) # Json as a big ol' list

pool = multiprocessing.Pool() #use all available cores, otherwise specify the number you want as an argument
pool.map(explode, range(len(data)))

end = time.time()
time_taken = (end-start)
print("Finished in:", time_taken)