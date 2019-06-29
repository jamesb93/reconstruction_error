# https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py

# https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html#sphx-glr-auto-examples-cluster-plot-affinity-propagation-py
from itertools import cycle
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from databending_utilities import read_json, write_json, get_path
import os

root = get_path()
pca = read_json(os.path.join(root, 'pca.json'))

classification = read_json(os.path.join(root, 'classification.json'))

### Filter to only get the values that from 'good' audio
labels = classification['1']

values = []
for key in labels:
    values.append(pca[key])

X = np.array(values)
# X = StandardScaler().fit_transform(data)
#############################################################################
# Compute DBSCAN
db = DBSCAN(eps=0.01, min_samples=4, n_jobs=-1).fit(X)

cluster_dict = {}
for audio, cluster in zip(labels, db.labels_):
    if str(cluster) in cluster_dict:
        cluster_dict[str(cluster)].append(audio)
    else:
        cluster_dict[str(cluster)] = [audio]

write_json(os.path.join(root, 'clusters.json'), cluster_dict)

# # Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
print(n_clusters_)
# n_noise_ = list(labels).count(-1)

# #############################################################################
