import os
from databending_utilities import get_path

root = get_path()

unique_audio_folder = os.path.join(root, 'DataAudioUnique')

unique_audio_files = os.listdir(unique_audio_folder)

for file in unique_audio_files:
    if file[0] == '.':
        os.rename(
            os.path.join(unique_audio_folder, file), 
            os.path.join(unique_audio_folder, file[1:])
            )





