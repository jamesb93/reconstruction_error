import os
import subprocess
from shutil import copyfile
from databending_utilities import * # import all from the utilities script

def convert(infile, outfile, encoding, bits, channels):
    subprocess.Popen(['sox', '-r', '44100', '--encoding', encoding, '-b', bits, '-c', channels, infile, outfile])

def mass_crawl():
    current_size = 0.0
    crawler = os.walk('/Users/jamesbradbury')
    for root, dirs, files in crawler:
        for x in files:
            # Make paths/dirs
            full_path = os.path.join(root, x)
            raw_path = os.path.join(raw_dir, f'{x}.raw')
            audio_path = os.path.join(audio_dir, f'{x}.wav')
            
            # Do checks
            if current_size < mb_lim:
                if check_size(full_path) and check_ext(full_path, bad_exts):
                    copyfile(full_path, raw_path) 
                    current_size += bytes_to_mb(os.path.getsize(raw_path))
                    if current_size < mb_lim:
                        convert(infile=raw_path, outfile=audio_path, encoding='signed-integer', bits='8', channels='1')


raw_dir   = '/Users/jamesbradbury/dev/data_bending/DataCopy/'
audio_dir = '/Users/jamesbradbury/dev/data_bending/DataAudio/'
mb_lim = 10000
bad_exts = ['.mov', '.avi', '.wmv', '.webm', '.flv', '.sock', '.wav', '.aiff', '.aif', '.mp3', '.mp4', '.wav', '.flac']
wipe_dir(raw_dir)
wipe_dir(audio_dir)
mass_crawl()

# print(check_ext('/Users/jamesbradbury/Sync/0_Max/Data/AEC.pdf', bad_exts))
# print(check_size('/Users/jamesbradbury/Library/Saved Application State/com.giorgiocalderolla.Wipr-Mac.savedState'))
