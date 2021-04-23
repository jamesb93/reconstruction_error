from pathlib import Path
import scipy.io.wavfile as wav


files = [x for x in Path("DataAudio").iterdir() if x.suffix == ".wav"]

s = 0
for z in files:
    rate, sig = wav.read(z)
    s += len(sig) / float(rate)

print(s)
