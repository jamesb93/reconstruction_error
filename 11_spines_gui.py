#####
# Using a KDTree - look at some 'spines' which can be considered exemplars
# Next, find other values which have similar close vector information to them, to identify groups of samples
####
import PySimpleGUI as sg
import numpy as np
from databending_utilities import read_json, write_json, get_path, walkman
import os
from sklearn.neighbors import KDTree

root = get_path()
spine_folder = os.path.join(root, 'spines')
spine_files = os.listdir(spine_folder)

print('Loading JSON data.')## Analysis Data ##
# shape_json = read_json(os.path.join(root, 'shape.json'))
pca_json   = read_json(os.path.join(root, 'pca.json'))
# simpledesc_json = read_json(os.path.join(root, 'simpledesc.json'))
# mfcc_raw_json = read_json(os.path.join(root, 'mfcc_nohpss.json'))
# mfcc = read_json(os.path.join(root, 'mfcc.json'))

# K Means to Find the closest neighbours depending on some features to a chosen file in the spines ##
feature = pca_json# <--- Change this feature here


# First, convert our feature data into a numpy array where the index is associated to the original dict.
data = [v for v in feature.values()]
keys = [k for k in feature.keys()]
data = np.array(data)

# Normalisation
data_min = np.amin(data)
data_max = np.amax(data)
data = (data - data_min) / (data_max - data_min)

# Select a file using an idx
idx = 70
spine = spine_files[idx]
print(f'Playing {spine}.')
# walkman(os.path.join(root, 'DataAudioUnique', spine))

# Now actually doing the tree calculation 
tree = KDTree(data, leaf_size=15)              
dist, ind = tree.query([data[idx]], k=3)                

# print('The matches...')
# for matches in ind[0]:
#     walkman(os.path.join(root, 'DataAudioUnique', keys[matches]))
#     print(data[matches])

# print('And now the original data...')
# print(data[idx])


## Excellent Matches ##
# 23, 




