from datamosh.utils import read_json, write_json
import os
import csv

f = read_json("/Users/jamesbradbury/dev/data_bending/python_scripts/dimensionality_reduction/outputs/UMAP_2001/umap.json")

values = [x for x in f.values()]

master_dict = {
    "data" : []
}
print(master_dict)

for value in values:
    t_dict = {}
    t_dict["x"] = value[0]
    t_dict["y"] = value[1]
    master_dict["data"].append(t_dict)

master_dict.update(t_dict)
write_json("json_data.json", master_dict)





