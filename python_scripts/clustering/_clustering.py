# https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py
import sys
import numpy as np
import os
import hdbscan
import random
from shutil import copyfile
from sklearn.cluster import DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from datamosh.utils import read_json, write_json,read_yaml, printp, check_make
from datamosh.variables import project_root, analysis_data


if len(sys.argv) != 2:
    print('You need to pass a YAML config file as an argument.')
    exit()

this_script = os.getcwd()

# Configuration
printp('Reading configuration')
cfg_path = os.path.join(this_script, sys.argv[1])
cfg = read_yaml(cfg_path)
json_out      = cfg['json']
input_data    = cfg['input_data']
algorithm     = cfg['algorithm']
normalisation = cfg['normalisation']
tog_plot      = cfg['tog_plot']
identifier    = cfg['identifier']


folder_name = f'{algorithm}_{identifier}'
output_path = os.path.join(this_script, 'outputs', folder_name)
check_make(output_path)
copyfile(cfg_path, os.path.join(output_path, 'configuration.yaml'))

printp('Reading in data')
feature = read_json(os.path.join(project_root, 'python_scripts', 'dimensionality_reduction', 'outputs', input_data))
keys    = [x for x in feature.keys()]
values  = [y for y in feature.values()]

data = np.array(values)

if normalisation != 'none':
    if normalisation == 'minmax':
        scaler = MinMaxScaler()
    if normalisation == 'standardise':
        scaler = StandardScaler()
    scaler.fit(data)
    data = scaler.transform(data)

if algorithm == 'AP':
    ap_n_clusters = cfg['ap_n_clusters']
    db = AgglomerativeClustering(n_clusters=ap_n_clusters).fit(data)
if algorithm == 'DBSCAN':
    db = DBSCAN(eps=0.01, min_samples=4, n_jobs=-1).fit(data)
if algorithm == 'HDBSCAN':
    db = hdbscan.HDBSCAN().fit(data)

cluster_dict = {}
# extract the label provided by the instance of DBSCAN (labels found in db.labels_)
# make a dict out of th is information
for audio, cluster in zip(keys, db.labels_):
    if str(cluster) in cluster_dict:
        cluster_dict[str(cluster)].append(audio)
    else:
        cluster_dict[str(cluster)] = [audio]

write_json(os.path.join(output_path, json_out), cluster_dict)