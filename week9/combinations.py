mod = 10**9 + 7
n, x = map(int, input().split())
coins = list(map(int, input().split()))
dp = [0] * (x + 1)
dp[0] = 1
# For each coin, update dp[j] for sums j from coin to x.
for coin in coins:
    for j in range(coin, x + 1):
        dp[j] = (dp[j] + dp[j - coin]) % mod
print(dp[x])
