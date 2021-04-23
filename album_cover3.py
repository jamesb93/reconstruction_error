from PIL import Image
from pathlib import Path
import numpy as np
import math
from random import randint
import json


w, h = 1800, 1800
bs = 1 # brush size

def read_json(json_file_path: str) -> dict:
    """Takes a JSON file and returns a dictionary"""
    with open(json_file_path, "r") as fp:
        data = json.load(fp)
        return data


data = read_json("umap.json")
def make_image(plot):
    
    c = [256, 256, 256]
    blank = np.full((w, h, 3), 255).astype('uint8')

    for v in plot.values():
        x = v[0]
        y = v[1]
        x = round(w * x) -1
        y = round(h * y) -1
        
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
    img.save("umap.png")

make_image(data)

            

    

