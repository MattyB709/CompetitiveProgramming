import math
import queue
n, m, s, t = map(int,input().split())
class Vertex:
    def __init__(self, index):
        self.edge_list = [0] * (n + 1) #tradeoff to be made here between fast indexing vs fast iterating
        self.dist_s = math.inf
        self.index = index
        self.dist_t = math.inf

    def add_edge(self, edge):
        self.edge_list[edge] = 1

    def get_dist(self, s):
        return self.dist_s if s else self.dist_t
    def set_dist(self, s, dist):
        if s:
            self.dist_s = dist
        else:
            self.dist_t = dist

vertices = [Vertex(i) for i in range(n + 1)]
# instantiate vertices
for _ in range(m):
    v1, v2 = map(int,(input().split()))
    vertices[v1].add_edge(v2)
    vertices[v2].add_edge(v1)

def breadth_search(source: Vertex, s: bool):
    q = queue.SimpleQueue()
    q.put((source, 0))
    while not q.empty():
        v, dist = q.get()
        if (math.isinf(v.get_dist(s))):
            v.set_dist(s, dist) 
            for i, num in enumerate(v.edge_list):
                if num == 1:
                    q.put((vertices[i], dist + 1))
    
breadth_search(vertices[s], True)
breadth_search(vertices[t], False)
min_dist = vertices[s].dist_t
count = 0
for i in range(1, n):
    for j in range(i+1, n+1):
        if vertices[i].edge_list[j] == 1:
            continue
        dist = vertices[i].dist_s + vertices[j].dist_t + 1
        dist2 = vertices[j].dist_s + vertices[i].dist_t + 1
        if dist >= min_dist and dist2 >= min_dist:
            count += 1
            
print(count)

