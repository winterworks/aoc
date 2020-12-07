import re
import numpy as np
import itertools

data_file = open('./data/data7')
data = data_file.read().split('\n')
data_file.close()

def parse_rules(rule_row):
    parts = re.split(' bags contain | bags?, | bags?.', rule_row)
    result = []
    for part in parts[1:-1]:
        [weight, node] = part.split(' ', 1)
        if weight.isdigit():
            result.append([parts[0], node, int(weight)])
    return result

def find_edges(graph, look_for_nodes, col):
    edges = list(filter(lambda edge: edge[1 - col] in look_for_nodes, graph))
    if len(edges):
        new_edges = find_edges(graph, np.array(edges)[:,col], col)
        if new_edges is not None:
            for new_edge in new_edges:
                edges.append(new_edge)
        return np.array(edges, dtype=object)

def count_children(graph, node):
    children = np.array(list(filter(lambda edge: edge[0] == node, graph)))
    sum = 1
    for child in children:
        sum += count_children(graph, child[1]) * child[2]
    return sum

graph_map = map(parse_rules, data)
graph = np.array(list(itertools.chain(*list(graph_map))), dtype=object)
unique_nodes = np.unique(find_edges(graph, ['shiny gold'], 0)[:,0])
edges = find_edges(graph, ['shiny gold'], 1)

print(len(unique_nodes))
print(count_children(graph, 'shiny gold')-1)