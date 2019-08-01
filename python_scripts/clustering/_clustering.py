# https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py
# https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html#sphx-glr-auto-examples-cluster-plot-affinity-propagation-py
import sys
sys.path.append('../')
from itertools import cycle
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
from databending_utilities import read_json, write_json, get_path, read_yaml, norm_np
from db_vars import analysis_data
import os

if len(sys.argv) != 2:
    print('You need to pass a YAML config file as an argument.')
    exit()

this_script = os.getcwd()

# Configuration
cfg_path = os.path.join(this_script, sys.argv[1])
cfg = read_yaml(cfg_path)
json_out      = cfg['json']
input_data    = cfg['input_data']
algorithm     = cfg['algorithm']
tog_plot      = cfg['plot']

feature = read_json(os.path.join(analysis_data, input_data))
keys = [x for x in feature.keys()]
values = [y for y in feature.values()]


data = np.array(values)
data_norm = StandardScaler().fit_transform(data)
# Compute DBSCAN
db = DBSCAN(eps=0.01, min_samples=4, n_jobs=-1).fit(data_norm)

cluster_dict = {}

# extract the label provided by the instance of DBSCAN (labels found in db.labels_)
# make a dict out of th is information
for audio, cluster in zip(keys, db.labels_):
    if str(cluster) in cluster_dict:
        cluster_dict[str(cluster)].append(audio)
    else:
        cluster_dict[str(cluster)] = [audio]

write_json(os.path.join(this_script, json_out), cluster_dict)

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
print(n_clusters_)
