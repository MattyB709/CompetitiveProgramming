import math
import heapq

class Edge:
    def __init__(self, weight, dest):
        self.weight = weight
        self.dest = dest

class Vertex:
    def __init__(self, city):
        self.edge_list = []
        self.dist = math.inf
        self.city = city
        self.visited = False
    
    def add_edge(self, edge: Edge):
        self.edge_list.append(edge)
    
    def __str__(self):
        return f"{i}", self.city
    

first_line = list(map(int, input().split()))
n = first_line[0]
m = first_line[1]

vertices = [Vertex(i) for i in range(n)]

for i in range(m):
    line = list(map(int, input().split()))
    edge = Edge(line[2], line[1]-1)
    vertices[line[0]-1].add_edge(edge)

pq = []
heapq.heappush(pq, (0,0))
while len(pq) > 0:
    dist, dest = heapq.heappop(pq)
    vertex = vertices[dest]
    # check if we've hit this
    if math.isinf(vertex.dist):
        # first time hitting this
        vertex.dist = dist
    else:
        # if we've hit this before SKIP
        continue

    for edge in vertex.edge_list:
        heapq.heappush(pq, (dist+edge.weight, edge.dest))

for vertex in vertices:
    print(vertex.dist, end = " ")