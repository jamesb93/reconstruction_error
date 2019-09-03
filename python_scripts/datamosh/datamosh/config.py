from datamosh.utils import read_yaml

class Configuration():
    '''
    This class acs as a container 
    '''
    def __init__(self):
        self.yaml_file  = None

        self.json_out   = None
        self.input_data = None
        self.algorithm = None
        self.normalisation = None
        self.tog_plot = None
        self.identifier = None
        self.pre_reduction = None
        self.wav_out = None
        self.umap_neighbours = None
        self.umap_mindist = None

    def load_config(self, yaml_path)
        self.yaml_file = read_yaml(yaml_path)

    def try_extract(self, parameter, key):
        try:

        except:

    def get_config(self):
        try_extract(self.json_out, self.yaml_file['json'])
        try_extract(self.input_data, self.yaml_file['json'])
        try_extract(self.algorithm, self.yaml_file['json'])
        try_extract(self.normalisation, self.yaml_file['json'])
        try_extract(self.tog_plot, self.yaml_file['json'])
        try_extract(self.identifier, self.yaml_file['json'])
        try_extract(self.pre_reduction, self.yaml_file['json'])
        try_extract(self.wav_out, self.yaml_file['json'])
        try_extract(self.umap_neighbours, self.yaml_file['json'])
        try_extract(self.umap_mindist, self.yaml_file['json'])

