a, b, c, x, y = map(int, input().split())
g = 0 if x < y else 1
flowers = []
flowers.append(a)
flowers.append(b)
waters = []
waters.append(x)
waters.append(y)

num_flowers = 0
while flowers[g] > 0 and c > 0:
    if c - waters[g] < 0:
        break
    c -= waters[g]
    flowers[g] -= 1
    num_flowers += 1

g = 1 if g == 0 else 0

while flowers[g] > 0 and c > 0:
    if c - waters[g] < 0:
        break
    c -= waters[g]
    flowers[g] -= 1
    num_flowers += 1

print(num_flowers)
