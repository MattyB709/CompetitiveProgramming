import math
import sys
n = int(input())
MOD = 10**9 + 7

MAX = 10**6
facts = [1] * (MAX + 1)
inv = [1] * (MAX + 1)

for i in range(1, MAX + 1):
    facts[i] = (i * facts[i-1] ) % MOD

inv[MAX] = pow(facts[MAX], MOD - 2, MOD)
for i in reversed(range(1, MAX)):
    inv[i] = inv[i+1]* (i+1) % MOD

for line in sys.stdin:

    a, b = map(int, line.split())
    result = (facts[a] * inv[a-b] * inv[b]) % MOD
    print(result)
