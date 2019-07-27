from databending_utilities import printp, printe, samps2ms, wipe_dir, read_json, write_json, norm_np, read_yaml, ds_store
import os
import json
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
import numpy as np
from scipy.io import wavfile
from db_vars import root, parent, essentia_analysis, essentia_json
import multiprocessing as mp
import sys
import osc_utils
import timeit

# OSC
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc import udp_client
from osc_utils import max_post

# function to extract the data from the yaml file


class DataContainer():
    def __init__(self):
        self.master_dict = {}
        self.match_string = []
        self.keys = []

    def extract(self, slash_filter, file_name):
        data = read_yaml(os.path.join(essentia_analysis, file_name))
        del data['metadata']
        self.master_dict[file_name[:-5]] = data
    
    def create_database(self, slash_filter, name):
        print(name)
        self.match_string = name
        self.keys = [] # clear list
        self.keys = [x for x in os.listdir(essentia_analysis) if self.match_string in x]
        printp('Clawing out the analysis from master files')

        if len(self.keys) != 0:
            [self.extract(x, self.master_dict) for x in self.keys]
            printp('Database formed')
        else:
            printe('No files found with that name')

    # def query(self, slash_filter, query):
        

# Constants for OSC configuration
ip = '127.0.0.1'
client_port = 5000
server_port = 5001

# Client that will send data to Max from Python over port 5000
client = udp_client.SimpleUDPClient(ip, client_port)

# Instantiate instances of our container classes
database = DataContainer()

# Server that will receive data from Max to python over port 5001
# Also all the possible messages that can be sent to the server '/message'
dispatcher = dispatcher.Dispatcher()
dispatcher.map('/subset', database.create_database)
# dispatcher.map('/query', database.query)

# Create the server
server = osc_server.ThreadingOSCUDPServer(
    (ip, server_port), dispatcher
)

printp('Booted Entrymatcher OSC Server.')
server.serve_forever()
