from datamosh.utils import get_path, ds_store, cd_up
import os

root = get_path()
parent = cd_up(root, 2)

# Slices of DataAudioUnique
unique_audio_folder = os.path.join(parent, 'DataAudioUnique')
unique_audio_files  = ds_store(os.listdir(unique_audio_folder))

# Full Audio Files
audio_folder = os.path.join(parent, 'DataAudio')
audio_files  = ds_store(os.listdir(audio_folder))

# Spines
spine_folder = os.path.join(parent, 'spines')
spine_files  = ds_store(os.listdir(spine_folder))

# Essentia Analysis
essentia_analysis = os.path.join(parent, 'essentia_analysis')
essentia_json = os.path.join(parent, 'analysis_data', 'essentia_analysis.json')

# Analysis Data
analysis_data = os.path.join(parent, 'analysis_data')

# Other
tmp = os.path.join(parent, 'tmp')
