import sys

s = sys.stdin.readline().strip()
n = len(s)

# prefix function π[i] = length of longest border of s[0..i]
pi = [0] * n
for i in range(1, n):
    j = pi[i - 1]
    while j and s[i] != s[j]:
        j = pi[j - 1]
    if s[i] == s[j]:
        j += 1
    pi[i] = j

# collect all border lengths by following π from the last position
borders = []
k = pi[-1]
while k:
    borders.append(k)
    k = pi[k - 1]

# output in increasing order
print(' '.join(map(str, reversed(borders))))