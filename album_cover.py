from PIL import Image
import numpy as np
import soundfile as sf
import math
import sys

def bufspill(audio_file_path: str):
    try:
        t_data, _ = sf.read(audio_file_path)
        return t_data.transpose()
    except RuntimeError:
        print(f'Error reading: {audio_file_path}')

# audio_data = bufspill('/Users/james/dev/data_bending/DataAUdio/sys-o.a.wav')
audio_data = bufspill('/Users/james/dev/data_bending/DataAUdio/libopenblas64_.dylib.wav')

w, h = 3840, 2160
data = np.zeros((h, w, 3), dtype=np.uint8)
linear_range = w + h
for x in range(w-1):
    for y in range(h-1):
        sample_range = ((x+1)*3) * y
        sample = audio_data[sample_range:sample_range+3]
        # scaled_sample = ((sample + 1) * 0.5) * 256
        scaled_sample = [x for x in sample * 128]
        # alpha = 
        try:
            data[y][x] = sample
        except IndexError:
            print('Index error at ', x, y)
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()