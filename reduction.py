from databending_utilities import get_path, samps2ms, wipe_dir
import os
import json
import multiprocessing
import time
import matplotlib.pyplot as plt
import scipy
import sklearn
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition

root = get_path()
descriptors_file = f'{root}/audio_slices_analysis.json'

with open(descriptors_file) as f:
    descriptors_json = json.load(f)

descriptors_list = list(descriptors_json.values())
labels_list = list(descriptors_json.keys())

X = np.array(descriptors_list)

########## Dimensionality Reduction ##########
X = StandardScaler().fit_transform(X) # Standardise Data
pca = decomposition.PCA(n_components=2)
pca.fit(X)
X = pca.transform(X)
plt.scatter(X[:, 0], X[:, 1], marker='1') #scatterplot the first value against the second
## Annotate Points ##
# for label, x, y, in zip(labels_list, X[:, 0], X[:, 1]):
#     plt.annotate(
#         label,
#         xy=(x, y), xytext=(-0, 0),
#         textcoords='offset points', ha='right', va='bottom',
#         bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5)
#     )

plt.show() #show plot

