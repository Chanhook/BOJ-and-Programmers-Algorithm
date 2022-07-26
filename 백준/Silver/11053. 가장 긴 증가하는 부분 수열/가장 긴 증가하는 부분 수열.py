import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n)]

for k in range(n):
    dp[k] = 1
    for i in range(k):
        # print(k,a[k],i,a[i])
        if a[i] < a[k]:
            # print("prev",dp)
            dp[k] = max(dp[k], dp[i] + 1)
            # print("next",dp)

print(max(dp))
