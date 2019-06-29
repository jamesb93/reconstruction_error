from databending_utilities import get_path, samps2ms, wipe_dir, read_json, write_json
import os
import json
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn import decomposition
import numpy as np
import plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.plotly as py
import plotly.graph_objs as go
from scipy.io import wavfile

root = get_path()
feature_json = read_json(os.path.join(root, 'simpledesc.json'))
classification = read_json(os.path.join(root, 'classification.json'))

## Filter to only get the values that from 'good' audio
labels_list = classification['1']

descriptors_list = []
for label in labels_list:
    descriptors_list.append(feature_json[label])

data = np.array(descriptors_list)


# ########## Dimensionality Reduction ##########

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

## Make a dict with normalised coordinates and indices of samples for Max ###
data_min = np.amin(data)
data_max = np.amax(data)

# Normalisation
data = (data - data_min) / (data_max - data_min)
out_dict = {}

for key, value in zip(labels_list, data):
    out_dict[key] = list(value)
write_json(os.path.join(root, 'pca.json'), out_dict)

# Write out pca data to stereo wav file
data = data.astype('float32')
wavfile.write(os.path.join(root, 'pca.wav'), 44100, data)
    

