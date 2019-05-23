import os
import subprocess
from shutil import copyfile

def check_size(path):
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

def convert(infile, outfile, encoding, bits, channels):
    subprocess.Popen(['sox', '-r', '44100', '--encoding', encoding, '-b', bits, '-c', channels, infile, outfile])

def mass_crawl():
    current_size = 0.0
    # Do the crawling
    crawler = os.walk('/Users/jamesbradbury')
    for root, dirs, files in crawler:
        for x in files:
            # Make paths/dirs
            full_path = os.path.join(root, x)
            raw_path = os.path.join(raw_dir, f'{x}.raw')
            audio_path = os.path.join(audio_dir, f'{x}.wav')
            
            # Do checks
            if check_size(full_path) and check_ext(full_path, bad_exts) and current_size < mb_lim:
                print(check_size(full_path))
                print(check_ext(full_path, bad_exts))
                print(current_size)
                print('All checks finished')
                copyfile(full_path, raw_path) 
                current_size += bytes_to_mb(os.path.getsize(raw_path))
                if current_size < mb_lim:
                    convert(infile=raw_path, outfile=audio_path, encoding='signed-integer', bits='8', channels='1')


raw_dir   = '/Users/jamesbradbury/Sync/0_MAX/Data/DataCopy/'
audio_dir = '/Users/jamesbradbury/Sync/0_MAX/Data/DataAudio/'
mb_lim = 30000
bad_exts = ['.mov', '.avi', '.wmv', '.webm', '.flv', '.sock']
wipe_dir(raw_dir)
wipe_dir(audio_dir)
mass_crawl()

# print(check_ext('/Users/jamesbradbury/Sync/0_Max/Data/AEC.pdf', bad_exts))
# print(check_size('/Users/jamesbradbury/Library/Saved Application State/com.giorgiocalderolla.Wipr-Mac.savedState'))
