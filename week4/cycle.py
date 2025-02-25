import math

class Vertex:
    def __init__(self, index):
        self.edge_list = []
        self.dist = math.inf
        self.index = index
    
class Edge:
    def __init__(self, weight, dest):
        self.weight = weight
        self.dest = dest

n, m = map(int, input().split())
vertices = [Vertex(i) for i in range(n)]
edge_list = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edge_list.append((a,b,c))

def search(cycle_check: bool, cycle_list):
    vertices[0].dist = 0
    cycle_found = False
    for vert in vertices:
        for source, dest, weight in edge_list:
            if vertices[source - 1].dist + weight < vertices[dest - 1].dist:
                vertices[dest - 1].dist = vertices[source - 1].dist + weight
                if (cycle_check):
                    cycle_list.append(source)
                    cycle_found = True
    return cycle_found

cycle_list = []
search(False, [])
cycle_found = search(True, cycle_list)
if cycle_found:
    print("YES")
    print(*cycle_list)
else:
    print("NO")

    
