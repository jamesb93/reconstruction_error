import sys
sys.path.append('../')
from databending_utilities import read_json, write_json, norm_np, printp, read_yaml, get_path
from db_vars import parent, root
import os
from sklearn import decomposition
from sklearn import manifold
import numpy as np
import plotly
from plotly.offline import download_plotlyjs, plot
import plotly.graph_objs as go
from scipy.io import wavfile


if len(sys.argv) != 2:
    print('You need to pass a YAML file as an argument.')
    exit()

# Configuration
cfg_path = os.path.join(get_path(), sys.argv[1])
cfg = read_yaml(cfg_path)
wav_out       = cfg['wav']
json_out      = cfg['json']
input_data    = cfg['input_data']
pre_reduction = cfg['pre_reduction']
algorithm     = cfg['algorithm']
tog_plot      = cfg['plot']

feature = read_json(os.path.join(parent, 'analysis_data', input_data))

raw_data = [v for v in feature.values()]
data = np.asarray(raw_data)
data = norm_np(data)
keys = [k for k in feature.keys()]

# ######### Initial Reduction ##########
printp('Performing PRE-Reduction')
pca = decomposition.PCA(n_components=pre_reduction)
data = pca.fit_transform(data)

######### Dimensionality Reduction ##########
printp('Performing POST-Reduction')
if algorithm == 'TSNE':
    reduction = manifold.TSNE(n_components=2)
if algorithm == 'ISOMAP':
    reduction = manifold.Isomap(n_components=2)
printp('Fitting Transform')
data = reduction.fit_transform(data)

if tog_plot:
    printp('Transposing Data')
    data_transposed = data.transpose() ## X as one list, Y as another
    data_transposed = np.ndarray.tolist(data_transposed)
    printp('Plotting')
    ### Plot ###
    plot([go.Scattergl(x=data_transposed[0], y=data_transposed[1], mode='markers')])

# Normalisation
printp('Normalising for JSON output')
data = norm_np(data)
out_dict = {}

printp('Outputting JSON')
for key, value in zip(keys, data):
    out_dict[key] = list(value)
write_json(os.path.join(root, 'pca.json'), out_dict)

printp('Outputting WAV')
data = data.astype('float32')
wavfile.write(os.path.join(root, 'isomap.wav'), 44100, data)