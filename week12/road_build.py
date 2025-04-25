import sys

class Node:
    def __init__(self, num):
        self.num = num
        self.size = 1
        self.root = num
        self.edge_list = []

    def add_edge(self, edge):
        self.edge_list.append(edge)

def set_root(root, node, visited):
    visited.add(node.num)
    node.root = root
    for edge in node.edge_list:
        if edge not in visited:
            set_root(root, cities[edge], visited)

    
    
def union(city_one, city_two, cities, graphs):
    if not cities[city_one].root == cities[city_two].root: 
        if cities[cities[city_one].root].size > cities[cities[city_two].root].size:
            root = cities[city_one].root 
            node = cities[city_two]
            cities[root].size += cities[cities[city_two].root].size
            if cities[city_two].root in graphs:
                graphs.remove(cities[city_two].root)
        else:
            root = cities[city_two].root
            node = cities[city_one]
            cities[root].size += cities[cities[city_one].root].size
            if cities[city_one].root in graphs:
                graphs.remove(cities[city_one].root)
        visited = set()
        set_root(root, node, visited)
        cities[city_one].add_edge(city_two)
        cities[city_two].add_edge(city_one)

n, m = map(int, input().split())

cities = [Node(i) for i in range(n+1)] 
graphs = set(range(1, n+1))

for line in sys.stdin:
    city_one, city_two = map(int, line.split())
    if cities[city_one] is None:
        cities[city_one] = Node(city_one)
    if cities[city_two] is None:
        cities[city_two] = Node(city_two)
    union(city_one, city_two, cities, graphs)

print(len(graphs) - 1)
graph = next(iter(graphs))
rest = graphs - {graph}
for g in rest:
    print(cities[g].root, cities[graph].root)
