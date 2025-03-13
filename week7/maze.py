import heapq
from collections import deque
# priority queue stores (num_free, row, col)
n,m,k = map(int, input().split())
maze = []
for _ in range(n):
    chars = list(input())
    maze.append(chars)

x_dir = [1,0,-1,0]
y_dir = [0,1,0,-1]

# def check_connected(i1, j1, i2, j2):
#     # print("i1 j1 ", i1, j1)
#     if i1 == i2 and j1 == j2:
#         return True
#     if i1 == -1 or i1 == n or j1 == -1 or j1 == m:
#         return False
#     if maze[i1][j1] == '.':
#         dirs = []
#         maze[i1][j1] = 'x'
#         if i1 < i2:
#             dirs.append(0)
#             dirs.append(2)
#             if j1 < j2:
#                 dirs.append(1)
#                 dirs.append(3)
#             else:
#                 dirs.append(3)
#                 dirs.append(1)
#         elif i2 > i1:
#             dirs.append(2)
#             dirs.append(0)
#             if j1 < j2:
#                 dirs.append(1)
#                 dirs.append(3)
#             else:
#                 dirs.append(3)
#                 dirs.append(1)
#         else: 
#             if j1 < j2:
#                 dirs.append(1)
#                 dirs.append(3)
#             else:
#                 dirs.append(3)
#                 dirs.append(1)
#             dirs.append(0)
#             dirs.append(2)

#         for num in dirs:
#             if check_connected(i1 + x_dir[num], j1 + y_dir[num], i2, j2):
#                 maze[i1][j1] = '.'
#                 return True
#         maze[i1][j1] = '.'
#     return False

def bfs(i1, j1, i2, j2):
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((i1, j1))
    while queue:
        c1, c2 = queue.popleft()
        if c1 == i2 and c2 == j2:
            return True
        if visited[c1][c2]:
            continue
        else:
            visited[c1][c2] = True
        for i in range(4):
            d1, d2 = c1+x_dir[i], c2+y_dir[i]
            if 0<=d1 < n and 0 <= d2 < m:
                if not visited[d1][d2] and maze[d1][d2] == '.':
                    queue.append((d1,d2))
    return False

def count_free(i,j):
    free = 0

    if i == -1 or i == n or j == -1 or j == m:
        return -1
    
    if maze[i][j] != '.':
        return -1
    
    if not i - 1 <= -1:
        if maze[i-1][j] == '.':
            free += 1
    if not i + 1 >= n:
        if maze[i+1][j] == '.':
            free += 1
    if not j +1 >= m:
        if maze[i][j+1] == '.':
            free += 1
    if not j - 1 <= -1:
        if maze[i][j-1] == '.':
            free += 1
    return free

heap = []

for i in range(n):
    for j in range(m):
        if maze[i][j] == '.':
            free = count_free(i,j)
            heapq.heappush(heap, (free, i, j))
            
def print_maze():
    for i in range(n):
        for j in range(m):
            print(maze[i][j], end="")
        print()

num_x_placed = 0
while len(heap) > 0:
    if num_x_placed == k:
        break
    free, i, j = heapq.heappop(heap)
    # print("i: ", i, "j: ", j, "free: ", free)

    if maze[i][j] == 'X':
        continue
    # print("test: ", free, i, j)
    if free == 0:
        maze[i][j] = 'X'
        num_x_placed += 1
        # print_maze()
    if free == 1:
        maze[i][j] = 'X'
        freeup = count_free(i, j-1)
        if freeup > -1: heapq.heappush(heap, (freeup, i, j-1))
        freedown = count_free(i, j+1)
        if freedown > -1: heapq.heappush(heap, (freedown, i, j+1)) 
        freeright = count_free(i+1, j)
        if freeright > -1: heapq.heappush(heap, (freeright, i+1, j))
        freeleft = count_free(i-1, j)
        if freeleft > -1: heapq.heappush(heap, (freeleft, i-1, j))
        num_x_placed += 1
        # print_maze()
    if free == 2:
        to_check = []
        maze[i][j] = 'X'
        freeup = count_free(i, j-1)
        if freeup > -1: 
            to_check.append((i+0, j-1))
            heapq.heappush(heap, (freeup, i, j-1))
        freedown = count_free(i, j+1)
        if freedown > -1: 
            # print(freedown)
            to_check.append((i+0,j+1))
            heapq.heappush(heap, (freedown, i, j+1))
        freeright = count_free(i+1, j)
        if freeright > -1: 
            # print(freeright)
            to_check.append((i+1, j+0))
            heapq.heappush(heap, (freeright, i+1, j))
        freeleft = count_free(i-1, j)
        if freeleft > -1: 
            to_check.append((i-1,j+ 0))
            heapq.heappush(heap, (freeleft, i-1, j))
        # if len(to_check) > 2:
            # print("ERROR")
        # print(to_check)
        # print("i, j: ",i, j)
        # print("start: ",to_check[0][0]," ", to_check[0][1])
        # print("end: ",to_check[1][0]," ", to_check[1][1])       
        if len(to_check) == 2:
            if not bfs(to_check[0][0], to_check[0][1], to_check[1][0], to_check[1][1]):
                maze[i][j] = '.'
                # print("Not connected")
            else:
                num_x_placed += 1
            # print_maze()
    
        # print("huh")

print_maze()