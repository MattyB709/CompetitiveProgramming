n = int(input())
MOD = 1000000007
D = [0] * n
A = [0] * n
A[0] = 1
for i in range(1, n):
    D[i] = A[i - 1] * 3
    A[i] = (A[i - 1] * 2 + D[i - 1]) % MOD

print(D[n-1] % MOD)