import os
import sys
import tempfile
import argparse
import subprocess
from shutil import copyfile, rmtree
from datamosh.variables import project_root
from datamosh.utils import check_make, check_size, check_ext, bytes_to_mb, printp

parser = argparse.ArgumentParser(description='Scrape your hard drive and convert any file type to audio.')
parser.add_argument('-l', '--limit', type=int, default=5000, help='Limit of data to scrape in megabytes')
parser.add_argument('-e', '--encoding', type=str, default='unsigned-integer', help='The encoding of the output from SoX')
parser.add_argument('-b', '--bits', type=str, default='8', help='The word length of the output file')
parser.add_argument('-c', '--channels', type=str, default='1', help='The number of channels in the output file')
parser.add_argument('-i', '--infolder', type=str, default='~/', help='The input folder to scrape')
parser.add_argument('-o', '--outfolder', type=str, help='The output folder for audio')
args = parser.parse_args()

if not args.outfolder or not args.infolder:
    print('Please provide a valid input/output folder!')
    exit()

BAD_EXTS = ['.mov', '.avi', '.wmv', '.webm', '.flv', '.sock', '.wav', '.aiff', '.aif', '.mp3', '.mp4', '.wav', '.flac']
MB_LIM = args.limit

def convert(infile, outfile, encoding, bits, channels):
    subprocess.Popen([
        'sox', 
        '-r', '44100', 
        '--encoding', encoding, 
        '-b', bits, 
        '-c', channels, 
        infile, outfile
    ])

def scrape(origin_directory, output_directory):
    current_size = 0.0
    crawler = os.walk(origin_directory)
    for root, dirs, files in crawler:
        for x in files:
            # Make paths/dirs
            x = x.replace(' ', '_')
            # get rid of dots at the start of a file
            if x[0] == '.':
                x = x[1:]
            full_path = os.path.join(root, x)
            raw_path = os.path.join(tmp_dir, f'{x}.raw')
            audio_path = os.path.join(output_directory, f'{x}.wav')
            
            # Do checks
            if current_size < MB_LIM:
                if check_size(full_path, 30000) and check_ext(full_path, BAD_EXTS):
                    copyfile(full_path, raw_path) 
                    current_size += bytes_to_mb(os.path.getsize(raw_path))
                    if current_size < MB_LIM:
                        convert(infile=raw_path, outfile=audio_path, encoding=args.encoding, bits=args.bits, channels=args.channels)

tmp_dir = tempfile.mkdtemp()
origin_dir = args.infolder
audio_dir = os.path.join(
    project_root,
    args.outfolder
)

check_make(audio_dir)
scrape(origin_dir, audio_dir)
rmtree(tmp_dir)
printp('Completed Scraping')