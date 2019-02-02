import numpy

with open('matrix.txt', 'r') as f:
    data_matrix = f.read()

    matrix = numpy.genfromtxt('matrix.txt', dtype='str')

nodes_list = []
nodes_dict = {}

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i == j:
            continue
        elif matrix[i, j] == '0':
            nodes_list.append(j)
    nodes_dict[i] = nodes_list
    nodes_list = []

# Find the density of the graph
all_edges = 0
for i in nodes_dict.values():
    all_edges += len(i)

total_edges = all_edges / 2
density = total_edges / len(nodes_dict.keys())
print(density)


# For each node in the graph, print all of its edges
# for i, j in nodes_dict.items():
#     print('Node', i, 'relates to nodes', j)


# Print all edges in the graph, but only print each edge once
# list_keys = nodes_dict.keys()
# for i in range(len(nodes_dict.keys())):
#     for j in nodes_dict[i]:
#         if j < i:
#             nodes_dict[i].remove(j)
#
# for i, j in nodes_dict.items():
#     print('Node', i, 'relates to nodes', j)
