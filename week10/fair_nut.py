import sys
from collections import deque
data = sys.stdin.buffer.read().split()
it = iter(data)
n = int(next(it))
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    u = int(next(it)); v = int(next(it))
    g[u].append(v)
    g[v].append(u)

depth = [0]*(n+1)
parent = [0]*(n+1)
dq = deque()
dq.append(1)
parent[1] = 0
depth[1] = 0
while dq:
    u = dq.popleft()
    for w in g[u]:
        if w == parent[u]:
            continue
        parent[w] = u
        depth[w] = depth[u] + 1
        dq.append(w)

L = (n+1).bit_length()
# up[i][u] will be the 2^i-th ancestor of u.
up = [[0]*(n+1) for _ in range(L)]
for u in range(1, n+1):
    up[0][u] = parent[u]
for i in range(1, L):
    up_i = up[i]
    up_im1 = up[i-1]
    for u in range(1, n+1):
        up_i[u] = up_im1[ up_im1[u] ]

# Function to get kth ancestor of node u.
def getAncestor(u, k):
    i = 0
    while k:
        if k & 1:
            u = up[i][u]
        k //= 2
        i += 1
    return u

# Function to compute LCA of nodes u and v.
def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    # Raise u so that depth[u] == depth[v].
    d = depth[u] - depth[v]
    i = 0
    while d:
        if d & 1:
            u = up[i][u]
        d //= 2
        i += 1
    if u == v:
        return u
    for i in range(L-1, -1, -1):
        if up[i][u] != up[i][v]:
            u = up[i][u]
            v = up[i][v]
    return parent[u]

q = int(next(it))
out_lines = []
for _ in range(q):
    a = int(next(it)); b = int(next(it)); c = int(next(it))
    # Calculate distance between a and b.
    Lca = lca(a, b)
    d = depth[a] + depth[b] - 2 * depth[Lca]
    if c >= d:
        # The sloth can reach b.
        out_lines.append(str(b))
    else:
        # Otherwise, determine the c-th node on the path from a to b.
        d1 = depth[a] - depth[Lca]  # distance from a to LCA
        if c <= d1:
            ans = getAncestor(a, c)
        else:
            # Find (d - c)-th ancestor from b.
            ans = getAncestor(b, d - c)
        out_lines.append(str(ans))
sys.stdout.write("\n".join(out_lines))
