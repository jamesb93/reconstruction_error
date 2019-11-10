from databending_utilities import samps2ms, wipe_dir, read_json, write_json, norm_np
import os
import json
## Number crunching
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
import numpy as np
from scipy.io import wavfile
from db_vars import root

# OSC
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc import udp_client
from osc_utils import max_post

class PCA():
    '''
    A class that receives a json file with feature data and reduces its dimensions to two
    '''
    def __init__(self, client_obj):
        self.feature = None
        self.keys = None
        self.values = None
        self.client = client_obj
        self.descriptors_list = []
        self.pca_data_transposed = None
        
    
    def load_feature(self, slash_filter, json_file):
        max_post(f'Loading JSON data: {json_file}.', self.client)
        self.feature = read_json(os.path.join(root, json_file))
        max_post(f'Separating keys and data in: {json_file}.', self.client)
        self.data = [v for v in self.feature.values()]
        self.data = np.array(self.data)
        self.keys = [k for k in self.feature.keys()]
        max_post(f'JSON Data loaded and cleaved in twain.', self.client)

    def normalise_cols(self, slash_filter):
        try:
            max_post('Normalising data.', self.client)
            self.data = norm_np(self.data)
        except:
            max_post('There is no data currently loaded.', self.client)
    
    def dim_reduction(self, slash_filter):

        scaler = StandardScaler()
        scaler.fit(self.data)  # Fit Data with StandardScaler() (get mean and stddev)
        self.data = scaler.transform(self.data)  # Transform original data set based on the .fita
        pca = decomposition.PCA(n_components=2)
        pca.fit(self.data)
        self.data = pca.transform(self.data)


        # Renormalise the data so that the values of our pca sit nicely on a grid.
        self.pca_data = norm_np(self.data)

        self.pca_data_transposed = self.pca_data.transpose()
        self.pca_data_transposed_aslist = self.pca_data_transposed.tolist()
        for x, y, names in zip(self.pca_data_transposed_aslist[0], self.pca_data_transposed_aslist[1], self.keys): 
            self.client.send_message('/data', [names, x, y])
            # self.client.send_message('/y', self.pca_data_transposed_aslist[1])
            # self.client.send_message('/x', self.pca_data_transposed_aslist[0])
            # self.client.send_message('/names', )
    # def plot(self,slash_filter, out_file):


    def plot(self, slash_filter):
        self.pca_data_transposed = self.pca_data.transpose()  # X as one list, Y as another
        self.pca_data_transposed = np.ndarray.tolist(self.pca_data_transposed)

        ### Plot ###
        plot([go.Scattergl(x=self.pca_data_transposed[0], y=self.pca_data_transposed[1], mode='markers')])

# Constants for OSC configuration
ip = '127.0.0.1'
client_port = 5000
server_port = 5001

# Client that will send data to Max from Python over port 5000
client = udp_client.SimpleUDPClient(ip, client_port)

# Instantiate instances of our container classes
bonsai = PCA(client)

# Server that will receive data from Max to python over port 5001
# Also all the possible messages that can be sent to the server '/message'
dispatcher = dispatcher.Dispatcher()
dispatcher.map('/feature', bonsai.load_feature)
dispatcher.map('/normalise', bonsai.normalise_cols)
dispatcher.map('/reduce', bonsai.dim_reduction)
dispatcher.map('/plot', bonsai.plot)
# dispatcher.map('/write', bonsai.write)

# Create the server
server = osc_server.ThreadingOSCUDPServer(
    (ip, server_port), dispatcher
)

print('Booting PCA OSC Server.')
max_post('Booting PCA OSC Server.', bonsai.client)
server.serve_forever()
    

