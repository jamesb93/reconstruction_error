#####
# Using a KDTree - look at some 'spines' which can be considered exemplars
# Next, find other values which have similar close vector information to them, to identify groups of samples
####
import numpy as np
import os
from databending_utilities import read_json, write_json, get_path, norm_np 
from sklearn.neighbors import KDTree
from db_vars import root
# OSC
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc import udp_client
from osc_utils import max_post

class Tree():
    '''
    A class that contains all of the feature data and corresponding methods for processing that data.
    '''
    def __init__(self, client_obj):
        self.feature = None
        self.keys = None
        self.data = None
        self.tree = None
        self.dist = None
        self.matches = None
        self.k = 3
        self.client = client_obj
    
    def load_feature(self, slash_filter, json_file):
        max_post(f'Loading JSON data: {json_file}.')
        self.feature = read_json(os.path.join(root, json_file))
        max_post(f'Separating keys and data in: {json_file}.')
        self.data = [v for v in self.feature.values()]
        self.data = np.array(self.data)
        self.keys = [k for k in self.feature.keys()]
        max_post(f'JSON Data loaded and cleaved in twain.')

    def normalise_cols(self, slash_filter):
        try:
            max_post('Normalising data.')
            self.data = norm_np(self.data)
        except:
            max_post('There is no data currently loaded.')
    
    def build_tree(self, slash_filter):
        self.tree = KDTree(self.data, leaf_size=15)
        max_post('Created KDTree.')

    def query(self, slash_filter, file_name):
        try:
            self.idx = self.keys.index(str(file_name))
        except ValueError:
            max_post(f'{file_name} is not in keys.')
        
        self.query_data = self.data[self.idx]
        self.dist, self.ind = self.tree.query([self.query_data], k=self.k)
        self.distances = self.dist.tolist()
        self.matches = self.ind.tolist()
        self.matches_names = []
        for matches in self.matches[0]:
            self.matches_names.append(self.keys[matches])

        self.client.send_message('/matches',   self.matches[0])
        self.client.send_message('/id',        self.matches_names)
        self.client.send_message('/distances', self.dist[0])
    
    def change_k(self, slash_filter, k):
        self.k = k
        max_post(f'Returning {k} matches now.')

# Constants for OSC configuration
ip = '127.0.0.1'
client_port = 5000
server_port = 5001

# Client that will send data to Max from Python over port 5000
client = udp_client.SimpleUDPClient(ip, client_port)

# Instantiate instances of our container classes
bonsai = Tree(client)

# Server that will receive data from Max to python over port 5001
# Also all the possible messages that can be sent to the server '/message'
dispatcher = dispatcher.Dispatcher()
dispatcher.map('/feature'  , bonsai.load_feature  )
dispatcher.map('/normalise', bonsai.normalise_cols)
dispatcher.map('/build'    , bonsai.build_tree    )
dispatcher.map('/query'    , bonsai.query         )
dispatcher.map('/k'        , bonsai.change_k      )

# Create the server
server = osc_server.ThreadingOSCUDPServer(
    (ip, server_port), dispatcher
    )

print('Booting OSC Server.')
max_post('Booting OSC Server.')
server.serve_forever()