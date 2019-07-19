from databending_utilities import samps2ms, wipe_dir, read_json, write_json, norm_np, read_yaml, ds_store
import os
import json
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
import numpy as np
import plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.plotly as py
import plotly.graph_objs as go
from scipy.io import wavfile
from db_vars import root, essentia_analysis
import multiprocessing as mp
import sys

def extract(idx):
    features = read_yaml(os.path.join(essentia_analysis, file_list[idx]))
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

keys = [x[:-5] for x in os.listdir(essentia_analysis)]
counter = 0

if __name__ == '__main__':

    raw_data = mp.Manager().list()

    file_list = ds_store(os.listdir(essentia_analysis))
    num_jobs = len(file_list)
    with mp.Pool() as pool:
        for i, _ in enumerate(
            pool.imap_unordered(extract, range(num_jobs))
            , 1):
            sys.stderr.write('\rdone {0:%}'.format(i/num_jobs))

    print('Finished Raw Data Concatenation')

    data = np.array(list(raw_data))

    ######### Dimensionality Reduction ##########

    scaler = StandardScaler()
    scaler.fit(data) # Fit Data with StandardScaler() (get mean and stddev)
    data = scaler.transform(data) # Transform original data set based on the .fita
    pca = decomposition.PCA(n_components=2)
    pca.fit(data)
    data = pca.transform(data)

    data_transposed = data.transpose() ## X as one list, Y as another
    data_transposed = np.ndarray.tolist(data_transposed)

    ### Plot ###
    plot([go.Scattergl(x=data_transposed[0], y=data_transposed[1], mode='markers')])

    # Normalisation
    data = norm_np(data)
    out_dict = {}

    for key, value in zip(keys, data):
        out_dict[key] = list(value)
    write_json(os.path.join(root, 'pca.json'), out_dict)

    # Write out pca data to stereo wav file
    data = data.astype('float32')
    wavfile.write(os.path.join(root, 'pca.wav'), 44100, data)
    

