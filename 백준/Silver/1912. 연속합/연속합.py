import sys

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))

dp = [-int(1e5)] * (n + 1)
dp[1] = arr[0]

for i in range(2, n + 1):
    dp[i] = max(dp[i - 1] + arr[i - 1], arr[i - 1])

print(max(dp))
