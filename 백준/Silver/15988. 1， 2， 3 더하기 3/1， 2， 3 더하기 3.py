import sys

input = sys.stdin.readline
tc = int(input().strip())

MAX = 1_000_001
MOD = 1_000_000_009
dp = [0 for _ in range(MAX)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for k in range(4, MAX):
    dp[k] = (dp[k - 1] + dp[k - 2] + dp[k - 3]) % MOD

for _ in range(tc):
    n = int(input().strip())
    print(dp[n])