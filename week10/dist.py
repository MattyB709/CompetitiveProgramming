import math
n, q = map(int, input().split())

class Vertex:
    def __init__(self, num):
        self.num = num
        self.edge_list = []
    def add_edge(self, edge):
        self.edge_list.append(edge)

class TreeNode:
    def __init__(self, num):
        self.num = num
        self.children = []
        self.parent = None
        self.depth = -1
    
    def add_child(self, child):
        self.children.append(child)    

    def add_parent(self, parent):
        self.parent = parent

def construct_tree(node, depth):
    nodes[node].depth = depth
    for edge in vertices[node].edge_list:
        nodes[edge].parent = node
        nodes[node].children.append(edge)
        # if node in vertices[edge].edge_list:
        vertices[edge].edge_list.remove(node)
        construct_tree(edge, depth + 1)

def print_tree(root, level=0):
    # Print the current node with indentation based on the current level.
    print("  " * level + str(root.num))
    # Recursively print all children, increasing the level.
    for child in root.children:
        print_tree(nodes[child], level + 1)


nodes = [None] * (n + 1)
vertices = [None] * (n + 1)
root = None
for _ in range(n - 1):
    vert1, vert2 = map(int, input().split())
    if root is None:
        root = vert1
    nodes[vert1] = TreeNode(vert1)
    nodes[vert2] = TreeNode(vert2)
    if vertices[vert1] is None:
        vertices[vert1] = Vertex(vert1)
        vertices[vert1].add_edge(vert2)
    else:
        vertices[vert1].add_edge(vert2)
    if vertices[vert2] is None:
        vertices[vert2] = Vertex(vert2)
        vertices[vert2].add_edge(vert1)
    else:
        vertices[vert2].add_edge(vert1)

construct_tree(root, 0)
# print_tree(nodes[root])
print("parent: ", nodes[7].children)
max_power = math.ceil(math.log2(n)) + 1
dp = [[-1] * (max_power) for _ in range(n + 1)]

for i in range(1, n+1):
    dp[i][0] = nodes[i].parent if nodes[i].parent is not None else -1

for j in range(1, max_power):
    for i in range(1, n+1):
        if dp[i][j-1] == -1:
            continue
        dp[i][j] = dp[dp[i][j-1]][j-1]

for _ in range(q):
    node_one, node_two = map(int, input().split())
    depth_difference = nodes[node_one].depth - nodes[node_two].depth
    distance = 0
    if depth_difference < 0:
        depth_difference *= -1
        distance += depth_difference
        jump = math.floor(math.log2(depth_difference))
        node_two = dp[node_two][jump]
        while nodes[node_two].depth < nodes[node_one].depth:
            node_two = nodes[node_two].parent #this shouldn't be none, cause only root has None for parent
    elif depth_difference > 0:
        distance += depth_difference
        jump = math.floor(math.log2(depth_difference))
        node_two = dp[node_one][jump]
        while nodes[node_two].depth > nodes[node_one].depth:
            node_one = nodes[node_one].parent 
    
    # find lca
    if nodes[node_one] == nodes[node_two]:
        print(distance)
        continue

    n1 = nodes[dp[node_one][1]]
    n2 = nodes[dp[node_two][1]]
    i = 0
    while nodes[dp[node_one][1 + i]] != nodes[dp[node_two][1 + i]]:
        i+= 1
    distance += 2**(i+1)
    i -= 1
    node_one = dp[node_one][1+i]
    node_two = dp[node_two][1+i]
    while node_one is not None and node_two is not None and node_one != node_two:
        node_one = nodes[node_one].parent
        node_two = nodes[node_two].parent
        distance += 2
    print(distance)