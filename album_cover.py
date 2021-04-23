from PIL import Image
from pathlib import Path
from flucoma.utils import get_buffer
from concurrent.futures import ThreadPoolExecutor, as_completed
import numpy as np
import math

audio_dir = Path("~/Cloud/Projects/DataBending/DataAudio").expanduser()
image_dir = Path("album_covers")
w, h = 1500, 1500

def make_image(audio_file):
    data = get_buffer(audio_file, 'numpy')
    p = image_dir / audio_file.name
    length = data.shape[0]
    
    if length < w * h:
        diff = (w * h) - length
        data = np.pad(data, (diff-1, 1), 'wrap')

    container = np.zeros(shape=(w, h, 3))
    for i, point in enumerate(data):
        x = i % w-1
        y = round((i+1) / h)
        try:
            scale = ((point + 1) * 0.5) * 256
            container[x][y] = [scale, scale, scale]
        except:
            pass

    img = Image.fromarray(container.astype('uint8'), 'RGB')
    img.save(p.with_suffix('.png'))

if __name__ == "__main__":
    files = [x for x in audio_dir.iterdir()]
    try:
        files.remove('.DS_Store')
    except ValueError:
        pass
    num_files = len(files)
    task = progress.add_task("Image Creation", total=num_files)
    for x in files:
        make_image(x)
    
