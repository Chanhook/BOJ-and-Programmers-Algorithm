import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    inp_w, inp_v = map(int, sys.stdin.readline().split())
    for j in range(1, k+1):
        if j < inp_w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(inp_v + dp[i-1][j-inp_w], dp[i-1][j])

print(dp[n][k])
