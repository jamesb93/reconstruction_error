import os
import json
from databending_utilities import get_path, ds_store, read_json, walkman, write_json
from sklearn.preprocessing import StandardScaler
import numpy as np
import sys
import simpleaudio as sa
from joblib import dump, load
import time
from db_vars import root, unique_audio_folder, models
np.set_printoptions(suppress=True)

mfcc = read_json(os.path.join(root, 'mfcc.json'))
noise_examples = ds_store(os.listdir(os.path.join(root, 'NoiseExamples')))
good_examples  = ds_store(os.listdir(os.path.join(root, 'GoodExamples')))
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
# X_norm = (X - X.min(0)) / X.ptp(0) ## Normalise each column of np array X

### Naive Bayes ###
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
# X = StandardScaler().fit_transform(X

### Logistic Regression ###
### \https://scikit-learn.org/stable/modules/multiclass.html
# from sklearn.linear_model import LogisticRegression
# clf = LogisticRegression()

# ### State Vector Macine ###
## https://neerajkumar.org/writings/svm/
# from sklearn import svm
# clf = svm.SVC(gamma='scale')

### MLP Neural Network ###
# from sklearn.neural_network import MLPClassifier
# clf = MLPClassifier()

start = time.time()
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

## Classification and JSON formation ##

classification_dict = {}
good_preds = []
bad_preds = []

for entry in mfcc:
    values = mfcc[entry]
    t_data = np.array(values)
    # t_data_norm = (t_data - t_data.min(0) / t_data.ptp(0))

    prediction = clf.predict([t_data])

    if prediction == 1:
        good_preds.append(entry)
        # walkman(os.path.join(unique_audio_folder, entry))
    elif prediction == 0:
        bad_preds.append(entry)

classification_dict['0'] = bad_preds
classification_dict['1'] = good_preds

write_json(os.path.join(root, 'classification.json'), classification_dict)

    # # Playback ##
    # if prediction == 0:
    #     print(f'{entry} classified as {prediction}.')
        
end = time.time()
total = end-start
print(total)
