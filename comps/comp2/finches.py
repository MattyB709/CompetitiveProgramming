import bisect
from collections import Counter

n, m = map(int, input().split())
finches = []
for _ in range(n):
    l, h = map(int, input().split())
    finches.append((l, h))


# map each altitude to a wind speed
maps_init = Counter()
for _ in range(m):
    a, w = map(int, input().split())
    maps_init[a] += w
    
altitudes = sorted(maps_init)

sum = 0
maps = {}
for i in range(len(altitudes)):
    sum+= maps_init[altitudes[i]]
    maps[altitudes[i]] = sum


final_list = []
for l, h in finches:
    index = bisect.bisect(altitudes, h)
    if index == 0:
        final_list.append(l)
    elif altitudes[index-1] == h:
        final_list.append(maps[altitudes[index-1]] * 2 - maps_init[altitudes[index- 1]] + l)
    else:
        final_list.append(maps[altitudes[index-1]] * 2 + l)
print(*final_list)

