import math
from tqdm import tqdm

mod = 13**14
g = 2
h = 170
m = math.ceil(math.sqrt(mod))
baby_steps = {}
# we want to write g^e as g^im + j, so store g^j in a dictionary for efficient retrieval
current = 1
for j in tqdm(range(m)):
    baby_steps[current] = j # store j like a hash map, g^j mod 13**14 = j
    current = (current * g) % mod

c = pow(2, -m, mod) # mod inverse of g^-m to try and find g^j values
y = h
e = -1 
for i in tqdm(range(m)):
    if y in baby_steps:
        j = baby_steps[y]
        e = j + m * i
        break
    y = (y * c) % mod

print(e)
