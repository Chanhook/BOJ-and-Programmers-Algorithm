import sys

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1:
            if j == 1:
                dp[i][j] = arr[i - 1]
            else:
                dp[i][j] = dp[i][j - 1] + arr[i - 1]
        else:
            if i > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i][j - i] + arr[i - 1], dp[i - 1][j])

print(dp[-1][-1])
