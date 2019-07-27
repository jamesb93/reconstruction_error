import numpy as np
import os
import subprocess as sub
import random
from databending_utilities import read_json, write_json, bufspill, fold, list_to_coll
from db_vars import root, unique_audio_files, unique_audio_folder, tmp
from math import e
import time
np.set_printoptions(suppress=True)

live_db_anal = read_json(os.path.join(root, 'live_db_analysis.json'))
keys = [k for k in live_db_anal.keys()]
values = [v for v in live_db_anal.values()]
print(min(values))
zipped = zip(keys, values)

test_data = values

LIMIT = 100000
COOL_RATE = 1
TEMPERATURE = LIMIT
NAYBORHOOD = 20
starting_pt = random.randint(0, len(test_data))
comparison_pt = int()
results = []
start = time.time()
while TEMPERATURE > 0:
    state = test_data[starting_pt] #value where we start
    # Make a random move and keep it in the range of the data
    comparison_pt = starting_pt + random.randint(NAYBORHOOD * -1, NAYBORHOOD)
    comparison_pt = fold(comparison_pt, 0, len(test_data) - 1)

    naybor = test_data[comparison_pt] # value that we test
    
    nrg_delta = abs(naybor - state)
    if nrg_delta >= 0: #if the change in energy is negative
        starting_pt = comparison_pt
    
    elif nrg_delta < 0:
        coef = e * (nrg_delta / TEMPERATURE)
        rand_float = random.uniform(0, 1)
        if coef > rand_float:
            starting_pt = comparison_pt
        elif coef < rand_float:
            starting_pt = starting_pt
    # print(state, naybor)
    results.append(starting_pt)
    TEMPERATURE -= COOL_RATE

print(test_data[starting_pt])
end = time.time()
file_order = [keys[x] for x in results]
out_file = os.path.join(root, 'Live-files-34.db_arranged.txt')

list_to_coll(file_order, out_file)

print(f'Time taken: {end - start}')



