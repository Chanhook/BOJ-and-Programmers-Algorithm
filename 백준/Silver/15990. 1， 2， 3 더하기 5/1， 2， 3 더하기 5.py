import sys

input = sys.stdin.readline

tc = int(input().strip())

MAX = 100001
MOD = 1000000009
dp = [[0, 0, 0, 0] for _ in range(MAX)]

dp[1][1] = 1  # 1
dp[2][2] = 1  # 2
dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1  # 1+2 2+1

for i in range(4, MAX):
    dp[i][1] = dp[i - 1][2] % MOD + dp[i - 1][3] % MOD
    dp[i][2] = dp[i - 2][1] % MOD + dp[i - 2][3] % MOD
    dp[i][3] = dp[i - 3][1] % MOD + dp[i - 3][2] % MOD

for _ in range(tc):
    n = int(input().strip())
    print(sum(dp[n]) % MOD)
