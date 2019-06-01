import os

def check_size(path):
    """
    Check's the size of a fyle in bytes.
    Returns true if the file has a size.
    Used to avoid empty files.
    """
    try:
        if os.path.getsize(path):
            return True
    except OSError:
        return False

def check_ext(path, extensions):
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