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
        self.intersect = city
    
    def add_edge(self, edge: Edge):
        self.edge_list.append(edge)
    
    def set_lights(self, r, g):
        self.g = g
        self.r = r
    
n, m = map(int, input().split())
vertices = [Vertex(i) for i in range(n)]
for i in range(n):
    r,g = map(int, input().split())
    vertices[i].set_lights(r, g)
for i in range(m):
    start, end, dist = map(int, input().split())
    vertices[start-1].add_edge(Edge(dist, end-1))

heap = []
heapq.heappush(heap, (0,0))
while len(heap) > 0:
    dist, dest = heapq.heappop(heap)
    vertex = vertices[dest]
    # print("dest: ", dest)
    # print("dist: ", dist)
    if math.isinf(vertex.dist):
        # first time hitting this
        vertex.dist = dist
    else:
        # if we've hit this before SKIP
        continue
    # print(vertex.edge_list)
    for e in vertex.edge_list:
        new_dist = dist + e.weight
        # If e.dest is not the destination, apply waiting logic
        if e.dest != n - 1:
            cycle = vertices[e.dest].r + vertices[e.dest].g
            mod = new_dist % cycle
            if mod >= vertices[e.dest].r:
                new_dist += (cycle - mod)
        heapq.heappush(heap, (new_dist, e.dest))


print(vertices[-1].dist)