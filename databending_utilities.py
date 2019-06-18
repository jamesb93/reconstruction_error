import os
from scipy.io import wavfile
import soundfile as sf
import json

def check_size(path, min_size):
    '''
    Check's the size of a fyle in bytes.
    Returns true if the file has a size.
    Used to avoid empty files.
    '''
    try:
        if os.path.getsize(path) >= min_size and os.path.getsize(path) <= 150000000:
            return True
    except OSError:
        return False

def check_ext(path, extensions):
    '''
    Given a path and a list of legal extensions it either returns false or true.
    '''
    ext = os.path.splitext(path)[1]
    try:
        dummy = extensions.index(ext)
    except ValueError:
        return True
    else:
        return False
    
def wipe_dir(dir):
    for file_name in os.listdir(dir):
        os.remove(os.path.join(dir, file_name))

def bytes_to_mb(val):
    return val * 0.000001

def get_path():
    return os.path.dirname(os.path.realpath(__file__))

def samps2ms(ms, sr):
    return (ms / sr) * 1000.0


def ms2samps(samples, sr):
    return (samples/1000) * sr

def ds_store(list_in):
    if '.DS_Store' in list_in:
        list_in.remove('.DS_Store')
    return list_in

def bufspill(audio_file):
    '''
    Reads an audio file and converts its content to a numpy array.

    Args:
        : A path to an audio file.
    Returns:
        A numpy array containing the data as 32 bit floating point numbers.
    '''
    try:
        t_data, _ = sf.read(audio_file)
        return t_data.transpose()
    except:
        print(f'Could not read: {audio_file}')

def write_json(json_file, in_dict):
    '''
    Takes a dictionary and writes it to JSON file.

    Args:
        json_file: A path to where the JSON file will be written.
        in_dict: A dictionary that will be saved as JSON.
    Returns:
        None
    '''
    with open(json_file, 'w+') as fp:
        json.dump(in_dict, fp, indent=4) 

def read_json(json_file):
    '''
    Takes a JSON file and returns a dictionary

    Args:
        json_file: A path to a JSON file that will be read.
    Returns:
        A python dictionary.
    '''
    with open(json_file, 'r') as fp:
        data = json.load(fp)
        return data

