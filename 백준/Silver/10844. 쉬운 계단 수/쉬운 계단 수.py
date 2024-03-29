import sys
mod = 1000000000
n = int(sys.stdin.readline().strip())

dp = [[0]*10 for i in range(101)]
dp[1] = [0]+[1]*9

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1] 
        elif j == 9:
            dp[i][j] = dp[i-1][j-1] 
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n])%mod)
