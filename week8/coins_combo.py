n, total = map(int, input().split())
coins = list(map(int, input().split()))
MOD = 1000000007
coins.sort()
sums = [0] * (total + 1)
sums[total] = 1
for i in reversed(range(total + 1)):
    for coin in coins:
        if i - coin < 0:
            break
        sums[i - coin] =  (sums[i-coin] +sums[i]) % MOD

print(sums[0] % MOD)