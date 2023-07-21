import sys

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))

dp = [1] * n

temp_max = 0
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            temp_max = max(dp[j], temp_max)
    dp[i] = temp_max + 1
    temp_max = 0

print(max(dp))