n = int(input().strip())
arr = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

count = max(dp)
lis = []

for i in range(n - 1, -1, -1):
    if dp[i] == count:
        lis.append(arr[i])
        count -= 1

for e in reversed(lis):
    print(e, end=' ')
