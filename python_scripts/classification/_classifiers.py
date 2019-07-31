import sys
sys.path.append('../')
import os
from databending_utilities import ds_store, read_json, walkman, write_json, cd_up, read_yaml
from db_vars import root, unique_audio_folder, models, analysis_data
from sklearn.preprocessing import StandardScaler
import numpy as np
import simpleaudio as sa
from joblib import dump, load
np.set_printoptions(suppress=True)

if len(sys.argv) != 2:
    print('You need to pass a YAML config file as an argument.')
    exit()

this_dir = os.getcwd()

# Configuration
cfg_path = os.path.join(this_dir, sys.argv[1])
cfg = read_yaml(cfg_path)
json_out      = cfg['json']
input_data    = cfg['input_data']
algorithm     = cfg['algorithm']
pre_train     = cfg['pre_train']
normalisation = cfg['normalisation']

input_data = read_json(os.path.join(analysis_data, input_data))
noise_examples = ds_store(os.listdir(os.path.join(this_dir, 'NoiseExamples')))
good_examples = ds_store(os.listdir(os.path.join(this_dir, 'GoodExamples')))
features  = []
label     = []

for i in range(len(noise_examples)):
    try:
        data = input_data[noise_examples[i]]
        features.append(data)
        label.append(0)
    except:
        print(f'Error: Possibly no analysis data for {noise_examples[i]}')

for i in range(len(good_examples)):
    try:
        data = input_data[good_examples[i]]
        features.append(data)
        label.append(1)
    except:
        print(f'Error: Possibly no analysis data for {good_examples[i]}')

features = np.array(features)
label    = np.array(features)

features_norm = norm_np(features)

### Select model ###
if algorithm == 'NB':
    ### Naive Bayes ###
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()

if algorithm == 'LR':
    ### Logistic Regression ###
    # https://scikit-learn.org/stable/modules/multiclass.html
    from sklearn.linear_model import LogisticRegression
    clf = LogisticRegression()

if algorithm == 'SVM':
    ### State Vector Macine ###
    # https://neerajkumar.org/writings/svm/
    from sklearn import svm
    clf = svm.SVC(gamma='scale')

if algorithm == 'MLP':
    ## MLP Neural Network ###
    from sklearn.neural_network import MLPClassifier
    clf = MLPClassifier()

# Pretraining
model_type = f'{clf.__class__.__name__}_model.joblib'

if pre_train:
    clf.fit(X, y)
    dump(clf, os.path.join(models, model_type))
    print('Training new model.')

if not pre_train:
    if os.path.isfile(os.path.join(models, model_type)):
        clf = load(os.path.join(models, model_type))
        print('Using an existing model.')
    else:
        clf.fit(X, y)
        dump(clf, os.path.join(models, model_type))

# # Classification and JSON formation
# classification_dict = {}
# good_preds = []
# bad_preds = []

# for entry in mfcc:
#     values = mfcc[entry]
#     t_data = np.array(values)
#     # t_data_norm = (t_data - t_data.min(0) / t_data.ptp(0))

#     prediction = clf.predict([t_data])

#     if prediction == 1:
#         good_preds.append(entry)
#         # walkman(os.path.join(unique_audio_folder, entry))
#     elif prediction == 0:
#         bad_preds.append(entry)

# classification_dict['0'] = bad_preds
# classification_dict['1'] = good_preds

out_file = os.path.join(this_dir, json_out)
write_json(out_file, classification_dict)

if playback:
    if prediction == 0:
        print(f'{entry} classified as {prediction}.')