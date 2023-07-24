import sys

input = sys.stdin.readline
n = int(input().strip())

arr = []
for _ in range(n):
    arr.append(int(input().strip()))

dp = [[0, 0, 0] for _ in range(n + 1)]
dp[1][1] = arr[0]

for i in range(2, n + 1):
    amount = arr[i - 1]
    dp[i][1] = dp[i - 1][0] + amount
    dp[i][2] = dp[i - 1][1] + amount
    dp[i][0] = max(dp[i - 1])

print(max(dp[n])) if n != 1 else print(arr[0])
