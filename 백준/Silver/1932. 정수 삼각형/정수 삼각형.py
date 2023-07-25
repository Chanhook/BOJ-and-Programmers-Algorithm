import sys

input = sys.stdin.readline

n = int(input().strip())
arr = []
for i in range(n):
    nums = list(map(int, input().split()))
    arr.append(nums + [0] * (n - i - 1))

dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[1][1] = arr[0][0]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        num = arr[i - 1][j - 1]
        if j == 1:
            dp[i][j] = dp[i - 1][j] + num
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + num
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + num

print(max(dp[n]))
