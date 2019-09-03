# https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html#sphx-glr-auto-examples-cluster-plot-dbscan-py
import sys
sys.path.append('../')
import numpy as np
import os
import hdbscan
import random
from shutil import copyfile
from bokeh.io import export_svgs
from bokeh.plotting import figure, output_file, show
from bokeh.embed import file_html
from bokeh.resources import CDN
from sklearn.cluster import DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from datamosh.utils import read_json, write_json,read_yaml, printp, mkdir
from datamosh.variables import parent, analysis_data


if len(sys.argv) != 2:
    print('You need to pass a YAML config file as an argument.')
    exit()

this_script = os.getcwd()

# Configuration
printp('Reading configuration')
cfg_path = os.path.join(this_script, sys.argv[1])
cfg = read_yaml(cfg_path)
json_out      = cfg['json']
input_data    = cfg['input_data']
algorithm     = cfg['algorithm']
normalisation = cfg['normalisation']
tog_plot      = cfg['tog_plot']
identifier    = cfg['identifier']


folder_name = f'{algorithm}_{identifier}'
output_path = os.path.join(this_script, 'outputs', folder_name)
mkdir(output_path)
copyfile(cfg_path, os.path.join(output_path, 'configuration.yaml'))

printp('Reading in data')
feature = read_json(os.path.join(parent, 'python_scripts', 'dimensionality_reduction', 'outputs', input_data))
keys    = [x for x in feature.keys()]
values  = [y for y in feature.values()]

data = np.array(values)

if normalisation != 'none':
    if normalisation == 'minmax':
        scaler = MinMaxScaler()
    if normalisation == 'standardise':
        scaler = StandardScaler()
    scaler.fit(data)
    data = scaler.transform(data)

if algorithm == 'AP':
    ap_n_clusters = cfg['ap_n_clusters']
    db = AgglomerativeClustering(n_clusters=ap_n_clusters).fit(data)
if algorithm == 'DBSCAN':
    db = DBSCAN(eps=0.01, min_samples=4, n_jobs=-1).fit(data)
if algorithm == 'HDBSCAN':
    db = hdbscan.HDBSCAN().fit(data)

if tog_plot:
    printp('Transposing Data')
    data_transposed = data.transpose() ## X as one list, Y as another
    # data_transposed = np.ndarray.tolist(data_transposed)
    printp('Making Colours')
    num_clusters = db.labels_.max()
    # assign a random colour to each cluster then make a flat list with the values
    palette = []
    r = lambda: random.randint(0, 255)
    for i in range(num_clusters):
        palette.append('#%02X%02X%02X' % (r(),r(),r()))

    colour_assign = []
    for audio, cluster in zip(keys, db.labels_):
        if cluster != -1:
            colour_assign.append(palette[cluster-1])
        else:
            colour_assign.append('#000000')
    printp('Plotting')
    TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
    plot_output_path = os.path.join('outputs', output_path, 'plot.html')
    plot_title = f'Clustering using the {algorithm} algorithm'
    output_file(
        plot_output_path, 
        title=plot_title, 
        mode="inline")

    plot = figure(
        tools=TOOLS,
        x_range=(0.0, 1.0), 
        y_range=(0.0, 1.0),
        plot_width = 800,
        plot_height= 800,
        toolbar_location='below',
        title=plot_title)

    plot.output_backend='webgl'
    plot.scatter(data_transposed[0], data_transposed[1], radius=0.001, fill_alpha=0.6, line_color=None, fill_color=colour_assign)
    export_svgs(plot, filename=os.path.join(output_path, 'plot.svg'))
    show(plot)

cluster_dict = {}
# extract the label provided by the instance of DBSCAN (labels found in db.labels_)
# make a dict out of th is information
for audio, cluster in zip(keys, db.labels_):
    if str(cluster) in cluster_dict:
        cluster_dict[str(cluster)].append(audio)
    else:
        cluster_dict[str(cluster)] = [audio]

write_json(os.path.join(output_path, json_out), cluster_dict)
