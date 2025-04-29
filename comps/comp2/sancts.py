n, k, q = map(int, input().split())

finch_parents = [i for i in range(n)]
class_sizes = [1] * n

def find(id):
    while finch_parents[id] != id:
        finch_parents[id] = finch_parents[finch_parents[id]]
        id = finch_parents[id]
    return id
finches_genes = []
for _ in range(n):
    finches_genes.append(input())

