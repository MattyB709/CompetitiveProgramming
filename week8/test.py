MOD = 10**9 + 7
n, x = map(int, input().split())
coins = list(map(int, input().split()))

dp = [0] * (x + 1)
dp[0] = 1

for i in range(x + 1):
    for coin in coins:
        nxt = i + coin
        if nxt <= x:
            dp[nxt] = (dp[nxt] + dp[i]) % MOD

print(dp[x])
