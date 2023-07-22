n = int(input().strip())

dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i):
        if j * j > i:
            break
        dp[i] = min(dp[i - j * j] + 1, dp[i])

print(dp[n])