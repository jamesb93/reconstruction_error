import sys
import os
from datamosh.utils import read_json, write_json, read_json, cd_up, read_yaml, lines_to_list, printp
from datamosh.variables import unique_audio_folder, analysis_data
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np
np.set_printoptions(suppress=True)

if len(sys.argv) != 2:
    print('You need to pass a YAML config file as an argument.')
    exit()

this_dir = os.path.dirname(os.path.realpath(__file__))

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
noise_examples = lines_to_list(
    os.path.join(
        this_dir,
        'noise_examples.txt'
    )
)
good_examples = lines_to_list(
    os.path.join(
        this_dir,
        'good_examples.txt'
    )
)

features  = []
label     = []

printp('Creating classification labels')
# This creates two lists, which are inextricably linked.
# The features contain the data and at the same index of the label list, there is a label.
for example in noise_examples:
    try:
        data = input_data[example]
        features.append(data)
        label.append(0)
    except:
        print(f'Error: Possibly no analysis data for {example}')

for example in good_examples:
    try:
        data = input_data[example]
        features.append(data)
        label.append(1)
    except:
        print(f'Error: Possibly no analysis data for {example}')

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
    from sklearn.svm import SVC
    clf = SVC(gamma='auto')

if algorithm == 'linSVC':
    from sklearn.svm import LinearSVC
    clf = LinearSVC(random_state=0, tol=1e-5)

if algorithm == 'MLP':
    ## MLP Neural Network ###
    from sklearn.neural_network import MLPClassifier
    clf = MLPClassifier()

if algorithm == 'RF':
    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier(n_estimators=100,random_state=0, max_depth=1)

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