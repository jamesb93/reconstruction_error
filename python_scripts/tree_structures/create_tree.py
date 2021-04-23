import os
import networkx as nx
from datamosh.utils import read_json

this_script = os.path.dirname(os.path.realpath(__file__))
cluster_relationships = os.path.join(this_script, 'cluster_relationships')

g = nx.Graph()


layer_1 = read_json(
    os.path.join(cluster_relationships, 'cl_one.json' )
)

layer_2 = read_json(
    os.path.join(cluster_relationships, 'cl_two.json' )
)

layer_3 = read_json(
    os.path.join(cluster_relationships, 'cl_three.json' )
)

children_1 = layer_1.keys()

for child_1 in children_1:
    g.add_node(child_1)
    children_2 = 

# for child_1 in children_1:
#     g.add_node(child_1)








# nx.draw(g, with_labels=True, font_weight='bold')
# plt.show()