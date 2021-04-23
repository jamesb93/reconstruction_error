from databending_utilities import printp, samps2ms, wipe_dir, read_json, write_json, norm_np, read_yaml, ds_store
import os
import json
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
import numpy as np
from scipy.io import wavfile
from db_vars import root, parent, essentia_analysis, essentia_json
import multiprocessing as mp
import sys

## function to extract the data from the yaml file
def extract(file_name):
    features = read_yaml(os.path.join(
        parent, essentia_analysis, file_name))
    temp = []
    for key in features:
        if key != 'metadata' and key != 'dynamicComplexity' and key != 'loudness':
            for stat in features[key]:
                if type(features[key][stat]) == list:
                    [temp.append(x) for x in features[key][stat]]
                else:
                    temp.append(features[key][stat])
        elif key == 'dynamicComplexity' or key == 'loudness':
           temp.append(features[key])
    raw_data.append(temp)

if __name__ == '__main__':

    # Extract the live-db analysis ONLY
    match_string = 'Live-files'
    keys = []
    raw_data = []
    for x in os.listdir(essentia_analysis):
        if match_string in x:
            keys.append(x)

    raw_data = list()

    printp('Concatenating data frames together')
    [extract(x) for x in keys] # Flatten the data and store it in a master list
    
    printp('Starting PCA')

    data = np.array(list(raw_data))

    ######### Dimensionality Reduction ##########

    scaler = StandardScaler()
    scaler.fit(data)  # Fit Data with StandardScaler() (get mean and stddev)
    # Transform original data set based on the .fita
    data = scaler.transform(data)
    pca = decomposition.PCA(n_components=2)
    pca.fit(data)
    data = pca.transform(data)

    data_transposed = data.transpose()  # X as one list, Y as another
    data_transposed = np.ndarray.tolist(data_transposed)

    # Normalisation
    data = norm_np(data)
    out_dict = {}
    for key, value in zip(keys, data):
        out_dict[key[:-5]] = list(value)
    write_json(os.path.join(parent, 'sketches','livedb_pca.json'), out_dict)

    # Write out pca data to stereo wav file
    printp('Writing data to output files')
    data = data.astype('float32')
    wavfile.write(os.path.join(parent, 'sketches', 'livedb_pca.wav'), 44100, data)
    printp('Done')
