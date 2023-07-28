import sys

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])

reversed_arr = arr[::-1]
reversed_dp = [1] * n

for i in range(n):
    for j in range(i):
        if reversed_arr[i] > reversed_arr[j]:
            reversed_dp[i] = max(reversed_dp[j] + 1, reversed_dp[i])

max_len = 0
for x, y in zip(dp, reversed_dp[::-1]):
    max_len = max(x + y, max_len)

print(max_len - 1)
