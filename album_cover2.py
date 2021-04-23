from PIL import Image
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import numpy as np
import math
from random import randint
from flucoma.utils import get_buffer

audio_dir = Path("~/Cloud/Projects/DataBending/DataAudio").expanduser()
image_dir = Path("album_covers")
w, h = 1800, 1800
bs = 1 # brush size
    

def make_image(audio_file):
    data = get_buffer(audio_file, 'numpy')
    p = image_dir / audio_file.name
    c = [256, 256, 256]
    blank = np.full((w, h, 3), 255).astype('uint8')

    for x, y in zip(data, data[1:]):
        x = round(((x + 1) * 0.5) * (w))
        y = round(((y + 1) * 0.5) * (h))
        
        blank[x][y] = c
        if bs >= 1:
            for l in range(x-bs, x+1+bs):
                for r in range(y-bs, y+1+bs):
                    # state = randint(0, 1)
                    try:
                        # blank[l][r] = [z * state for z in c]
                        blank[l][r] = [256, 256, 256]
                    except:
                        pass
        # Trailing lines out from the points...

    img = Image.fromarray(blank, mode='RGB')
    print(img)
    img.save(p.with_suffix('.png'))

files = [x for x in audio_dir.iterdir()]

try: 
    files.remove('.DS_Store')
except ValueError: 
    pass


for x in files:
    make_image(x)
    progress.update(task, advance=1)

            

    

