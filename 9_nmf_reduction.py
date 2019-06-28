from databending_utilities import get_path, samps2ms, wipe_dir, read_json, write_json
import os
import json
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn import decomposition
import numpy as np
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from scipy.io import wavfile

root = get_path()
descriptors_json = read_json(os.path.join(root, 'nmf_mfcc.json'))

labels = list(descriptors_json.keys())
data = list(descriptors_json.values())

########## Dimensionality Reduction ##########
data = StandardScaler().fit_transform(data) # Standardise Data
pca = decomposition.PCA(n_components=2)
pca.fit(data)
data = pca.transform(data)

data_transposed = data.transpose() ## X as one list, Y as another

plot([go.Scattergl(x=data_transposed[0], y=data_transposed[1], mode='markers')])

### Make a dict with normalised coordinates and indices of samples for Max ###
data_min = np.amin(data)
data_max = np.amax(data)

# Normalisation
data = (data - data_min) / (data_max - data_min)
out_dict = {}

for key, value in zip(labels, data):
    out_dict[key] = list(value)
write_json(os.path.join(root, 'pca.json'), out_dict)

# Write out pca data to stereo wav file
data = data.astype('float32')
wavfile.write(os.path.join(root, 'nmf_pca.wav'), 44100, data)
    

