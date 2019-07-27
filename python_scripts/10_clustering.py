# https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py

# https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html#sphx-glr-auto-examples-cluster-plot-affinity-propagation-py
from itertools import cycle
import matplotlib.pyplot as plt
from sklearn.cluster import AffinityPropagation
from sklearn import metrics
import numpy as np

from databending_utilities import read_json, write_json, get_path
import os

root = get_path()
pca = read_json(os.path.join(root, 'pca.json'))

classification = read_json(os.path.join(root, 'classification.json'))

### Filter to only get the values that from 'good' audio
keys = classification['1']

values = []
for key in keys:
    values.append(pca[key])

data = np.array(values)
# # #############################################################################
# Compute Affinity Propagation
print('I am calculating the Affinity Propogation clusters.')
af = AffinityPropagation(max_iter=3).fit(data)
print('I calculated the Affinity Propogation.')
cluster_centers_indices = af.cluster_centers_indices_
labels = keys

n_clusters_ = len(cluster_centers_indices)
print(n_clusters_)

#############################################################################
# Plot result

plt.close('all')
plt.figure(1)
plt.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    class_members = labels == k
    cluster_center = data[cluster_centers_indices[k]]
    plt.plot(data[class_members, 0], data[class_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)
    for x in data[class_members]:
        plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
