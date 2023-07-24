import sys

input = sys.stdin.readline
n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n + 1)]

dp[1][0], dp[1][1], dp[1][2] = arr[0][0], arr[0][1], arr[0][2]

for i in range(2, n + 1):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i - 1][j]
        elif j == 1:
            dp[i][j] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i - 1][j]
        elif j == 2:
            dp[i][j] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i - 1][j]

print(min(dp[n]))