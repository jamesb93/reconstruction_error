import sys
sys.path.append('../')
import os
from databending_utilities import ds_store, read_json, walkman, write_json, cd_up, read_yaml, printp
from db_vars import root, unique_audio_folder, models, analysis_data
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np
np.set_printoptions(suppress=True)

if len(sys.argv) != 2:
    print('You need to pass a YAML config file as an argument.')
    exit()

this_dir = os.getcwd()

# Configuration
printp('Reading configuration')
cfg_path = os.path.join(this_dir, sys.argv[1])
cfg = read_yaml(cfg_path)
json_out      = cfg['json']
input_data    = cfg['input_data']
algorithm     = cfg['algorithm']
normalisation = cfg['normalisation']

printp('Reading in data')
input_data = read_json(os.path.join(analysis_data, input_data))
noise_examples = ds_store(os.listdir(os.path.join(this_dir, 'NoiseExamples')))
good_examples = ds_store(os.listdir(os.path.join(this_dir, 'GoodExamples')))
features  = []
label     = []

printp('Creating classification labels')
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


# convert features and labels to numpy arrays
features = np.array(features)
label    = np.array(label)

if normalisation != 'none':
    if normalisation == 'minmax':
        scaler = MinMaxScaler()
    if normalisation == 'standardise':
        scaler = StandardScaler()
    scaler.fit(features)
    features = scaler.transform(features)

# Select Model
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

if algorithm == 'RF':
    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier(max_depth=5, n_estimators=10, n_features=1)

if algorithm == 'linSVC':
    from sklearn.svm import LinearSVC
    clf = LinearSVC(random_state=0, tol=1e-5)

printp('Fitting Transform')
# Compute the fit
clf.fit(features, label)


# Classification and JSON formation
classification_dict = {}
good_predictions = []
bad_predictions = []

printp('Classifying new data')
for entry in input_data:
    values = input_data[entry]
    t_data = np.asarray(values)

    if normalisation != 'none':
        t_data = scaler.transform([t_data])
    else:
        t_data = [t_data]

    prediction = clf.predict(t_data)

    if prediction == 1:
        good_predictions.append(entry)
        # walkman(os.path.join(unique_audio_folder, entry))
    elif prediction == 0:
        bad_predictions.append(entry)

printp('Writing out classification to JSON')
classification_dict['0'] = bad_predictions
classification_dict['1'] = good_predictions

out_file = os.path.join(this_dir, json_out)
write_json(out_file, classification_dict)

