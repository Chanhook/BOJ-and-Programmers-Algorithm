import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(1, 1 << n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])
    if sum(subset) == s:
        ans += 1

print(ans)