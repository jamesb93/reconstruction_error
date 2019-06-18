import os
import json
from databending_utilities import *
import numpy as np
import sys
import simpleaudio as sa
np.set_printoptions(suppress=True)

root = get_path()
mfcc = read_json(os.path.join(root, 'mfcc.json'))
unique_audio_folder = os.path.join(root, 'DataAudioUnique')
noise_examples = os.listdir(os.path.join(root, 'NoiseExamples'))
noise_examples = ds_store(noise_examples)
good_examples = os.listdir(os.path.join(root, 'GoodExamples'))
good_examples = ds_store(good_examples)
X = []
y = []

for i in range(len(noise_examples)):
    data = mfcc[noise_examples[i]]
    X.append(data)
    y.append(i)

print(f'Bad Examples classified between 0 and {len(noise_examples)}.')

for i in range(len(good_examples)):
    data = mfcc[good_examples[i]]
    X.append(data)
    y.append(i+len(noise_examples))

print(f'Good Examples classified between {len(noise_examples)} and {len(good_examples) + len(noise_examples)}')

X = np.array(X)
y = np.array(y)

X_norm = (X - X.min(0)) / X.ptp(0) ## Normalise each column of np array X

### Naive Bayes ###
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

### Logistic Regression ###
# from sklearn.linear_model import LogisticRegression
# clf = LogisticRegression()

# ### State Vector Macine ###
# from sklearn import svm
# clf = svm.SVC(gamma='scale')
print(len(good_examples))
clf.fit(X, y)
for entry in mfcc:
    values = mfcc[entry]
    t_data = np.array(values)
    t_data_norm = (t_data - t_data.min(0) / t_data.ptp(0))

    prediction = clf.predict([t_data_norm])
    if prediction > len(noise_examples):

        print(entry, good_examples[int(prediction - len(noise_examples))], prediction)
        wave_obj = sa.WaveObject.from_wave_file(os.path.join(unique_audio_folder, entry))
        play_obj = wave_obj.play()
        play_obj.wait_done()



