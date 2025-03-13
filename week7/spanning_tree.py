from collections import deque
# priority queue stores (num_free, row, col)
n,m,k = map(int, input().split())
maze = []
for _ in range(n):
    chars = list(input())
    maze.append(chars)

parents = [[None] * m for _ in range(n)]
children_count = [[0] * m for _ in range(n)]
p1, p2 = 0,0
found_dot = False
for i in range(n):
    for j in range(m):
        if maze[i][j] == '.':
            p1, p2 = i,j
            found_dot = True
            break
    if found_dot:
        break

x_dir = [1,0,-1,0]
y_dir = [0,1,0,-1]

queue = deque()
queue.append((p1, p2))
visited = [[False] * m for _ in range(n)]
visited[p1][p2] = True
while len(queue) > 0:

    c1, c2 = queue.popleft()
    for i in range(4):
        d1, d2 = c1+x_dir[i], c2 + y_dir[i] 
        if 0 <= d1 < n and 0 <= d2 < m:
            if not visited[d1][d2] and maze[d1][d2] == '.':
                visited[d1][d2] = True
                parents[d1][d2] = (c1, c2)
                children_count[c1][c2] += 1
                queue.append((d1,d2))
        
lqueue = deque()
for i in range(n):
    for j in range(m):
        if children_count[i][j] == 0 and maze[i][j] == '.':
            lqueue.append((i, j))

num_x = 0
# for i in range(n):
#     for j in range(m):
#         print(children_count[i][j], end="")
#     print()
while num_x < k:
    c1, c2 = lqueue.popleft()
    # print("c1, c2: ", c1, c2)
    maze[c1][c2] = 'X'
    num_x += 1
    p1, p2 = parents[c1][c2]
    # print("p1, p2: ", p1, p2)
    children_count[p1][p2] -= 1
    # print("children count: ", children_count[p1][p2])
    if children_count[p1][p2] == 0:
        # print("appended")
        lqueue.append((p1,p2))

for i in range(n):
    for j in range(m):
        print(maze[i][j], end = "")
    print()
