import os

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
    return (ms/sr) * 1000.0

