from databending_utilities import samps2ms, wipe_dir, read_json, write_json, norm_np, read_yaml, ds_store, printp
import os
import json
from sklearn.preprocessing import StandardScaler
from sklearn import manifold
import numpy as np
import plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.plotly as py
import plotly.graph_objs as go
from scipy.io import wavfile
from db_vars import root, parent, essentia_analysis
import sys


analysis = read_json(os.path.join(parent, 'analysis_data', 'essentia_cat.json'))

keys = [x for x in analysis.keys()]
raw_data = [x for x in analysis.values()]

printp('Constructed Python Data type')

pre_data = np.array(list(raw_data))
data = np.nan_to_num(pre_data)

######### Dimensionality Reduction ##########
scaler = StandardScaler()
scaler.fit(data) # Fit Data with StandardScaler()
data = scaler.transform(data) # Transform original data set based on the .fita
isomap = manifold.Isomap(n_components=2)
isomap.fit(data)
data = isomap.transform(data)

data_transposed = data.transpose() ## X as one list, Y as another
data_transposed = np.ndarray.tolist(data_transposed)
printp('Completed Dimensionality Reduction')

# ### Plot ###
plot([go.Scattergl(x=data_transposed[0], y=data_transposed[1], mode='markers')])
printp('Plot Created')

# Normalisation
data = norm_np(data)
out_dict = {}

for key, value in zip(keys, data):
    out_dict[key] = list(value)
write_json(os.path.join(parent, 'analysis_data', 'isomap_essentia.json'), out_dict)
printp('Bounced to JSON file')