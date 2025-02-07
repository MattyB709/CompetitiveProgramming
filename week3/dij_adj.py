from queue import PriorityQueue
import math
list1 = list(map(int, input().split()))
n = list1[0]
m = list1[1]

adj = [[math.inf] * n for _ in range(n)]
cities = [0] * n

for i in range(m):
    line = list(map(int, input().split()))
    current = adj[line[0] - 1][line[1] - 1]
    adj[line[0] - 1 ][line[1] - 1] = line[2] if line[2]  < current else current
    
pq = PriorityQueue()
dist = 0
# THIS ONLY WORKS WITH NO SELF LOOPS
# this seems like a reasonable assumption for an airport
pq.put((dist,0))
while not pq.empty():
    dist, city = pq.get()

    # if not visited, mark as visited (-1) and update the distance, because we know we've found it
    if adj[city][city] == math.inf:
        adj[city][city] = -1
        cities[city] = dist
    else:
        # otherwise, SKIP
        continue
    # loop through all other paths from this city (O(N)...)
    for i in range(n):
        # if a path exists, add it to the pq
        if not adj[city][i] == math.inf:
            pq.put((dist+adj[city][i], i))

print(*cities)
