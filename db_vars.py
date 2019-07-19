from databending_utilities import get_path, ds_store
import os

root = get_path()
# Slices of DataAudioUnique
unique_audio_folder = os.path.join(root, 'DataAudioUnique')
unique_audio_files  = ds_store(os.listdir(unique_audio_folder))

# Full Audio Files
audio_folder = os.path.join(root, 'DataAudio')
audio_files  = ds_store(os.listdir(audio_folder))

# Spines
spine_folder = os.path.join(root, 'spines')
spine_files  = ds_store(os.listdir(spine_folder))

# NMF Folder
nmf_folder = os.path.join(root, 'DataAudioNMF')

# Essentia Analysis
essentia_analysis = os.path.join(root, 'essentia_analysis')

# Other
models = os.path.join(root, 'models')
tmp = os.path.join(root, 'tmp')
