import math

# Read input
n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a - 1, b - 1, c))

dist = [0] * n
parent = [-1] * n

x = -1  
# relax edges n times
for i in range(n):
    x = -1  
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            parent[v] = u
            x = v


if x == -1:
    print("NO")
else:
    for i in range(n):
        x = parent[x]
    
    # Reconstruct the cycle.
    cycle = []
    v = x
    while True:
        cycle.append(v)
        v = parent[v]
        if v == x:
            cycle.append(v)
            break
    cycle.reverse()  

    cycle = [v + 1 for v in cycle]

    print("YES")
    print(" ".join(map(str, cycle)))
