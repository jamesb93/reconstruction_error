import os
import json
from databending_utilities import get_path, ds_store, read_json
import numpy as np
import sys
import simpleaudio as sa
from joblib import dump, load
np.set_printoptions(suppress=True)

root = get_path()
mfcc = read_json(os.path.join(root, 'mfcc.json'))
unique_audio_folder = os.path.join(root, 'DataAudioUnique')
models = os.path.join(root, 'models')
noise_examples = os.listdir(os.path.join(root, 'NoiseExamples'))
noise_examples = ds_store(noise_examples)
good_examples = os.listdir(os.path.join(root, 'GoodExamples'))
good_examples = ds_store(good_examples)
X = []
y = []

for i in range(len(noise_examples)):
    try:
        data = mfcc[noise_examples[i]]
        X.append(data)
        y.append(0)
    except:
        print(f'Error: Possibly no analysis data for {noise_examples[i]}')

for i in range(len(good_examples)):
    try:
        data = mfcc[good_examples[i]]
        X.append(data)
        y.append(1)
    except:
        print(f'Error: Possibly no analysis data for {good_examples[i]}')

X = np.array(X)
y = np.array(y)
X_norm = (X - X.min(0)) / X.ptp(0) ## Normalise each column of np array X

### Naive Bayes ###
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()


### Taken from https://scikit-learn.org/stable/modules/multiclass.html
### Logistic Regression ###
# from sklearn.linear_model import LogisticRegression
# clf = LogisticRegression()

# ### State Vector Macine ###
## https://neerajkumar.org/writings/svm/
# from sklearn import svm
# clf = svm.SVC(gamma='scale')

### MLP Neural Network ###
# from sklearn.neural_network import MLPClassifier
# clf = MLPClassifier()

## Pretraining
model_type = f'{clf.__class__.__name__}_model.joblib'
pre_train = False ## If pre_train is 1, then an apprporiate pretrained model is loaded. Else, do it again and write the results out

if pre_train is False:
    clf.fit(X, y)
    dump(clf, os.path.join(models, model_type))
    print('Training new model.')

elif pre_train is True:
    if os.path.isfile(os.path.join(models, model_type)):
        clf = load(os.path.join(models, model_type))
        print('Using an existing model.')
    else:
        clf.fit(X, y)
        dump(clf, os.path.join(models, model_type))

## Classification
for entry in mfcc:
    values = mfcc[entry]
    t_data = np.array(values)
    t_data_norm = (t_data - t_data.min(0) / t_data.ptp(0))

    prediction = clf.predict([t_data_norm])
    if prediction == 1:
        print(f'{entry} classified as {prediction}.')
        wave_obj = sa.WaveObject.from_wave_file(os.path.join(unique_audio_folder, entry))
        play_obj = wave_obj.play()
        play_obj.wait_done()
