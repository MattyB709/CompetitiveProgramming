s = input().strip()
good_mask = input().strip()
k = int(input().strip())

good = [c == '1' for c in good_mask]     

nodes = [[-1] * 26]                       
distinct = 0

for i in range(len(s)):
    bad = 0
    v = 0                                 
    for j in range(i, len(s)):
        idx = ord(s[j]) - 97
        if not good[idx]:
            bad += 1
            if bad > k:                   
                break
        if nodes[v][idx] == -1:           
            nodes[v][idx] = len(nodes)
            nodes.append([-1] * 26)
            distinct += 1
        v = nodes[v][idx]                

print(distinct)
