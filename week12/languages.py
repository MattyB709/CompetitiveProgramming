import sys

n, m = map(int, input().split())

parents = [i for i in range(m+1)]
sizes = [0] * (m+1)
total = 0

def find_parent(x):

    while x != parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x

def dsu(lang1, lang2):
    parent1 = find_parent(lang1)
    parent2 = find_parent(lang2)
    if sizes[parent1] == 0:
        sizes[parent1] = 1
    if sizes[parent2] == 0:
        sizes[parent2] = 1

    if sizes[parent1] > sizes[parent2]:
        parents[parent2] = parent1
        sizes[parent1] += sizes[parent2]
    else:
        parents[parent1] = parent2
        sizes[parent2] += sizes[parent1]
    
for line in sys.stdin:
    langs = list(map(int, line.split()))
    num_langs = langs[0]
    if num_langs == 0:
        total += 1
    else:
        if sizes[langs[1]] == 0:
            sizes[langs[1]] = 1
        for i in range(2, num_langs+1):
            dsu(langs[1], langs[i])
    
sets = {find_parent(i) for i in parents if sizes[i] != 0}
# print(sets)
total += max(len(sets) - 1, 0)

print(total)