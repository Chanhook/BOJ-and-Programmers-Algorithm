import sys

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

cum = [0] * (n + 1)
for i in range(n):
    cum[i + 1] = cum[i] + arr[i]

if sum(arr) < s:
    print(0)
else:
    l = 0
    r = 1
    min_length = sys.maxsize
    while l <= r:
        cul_sum = cum[r] - cum[l]
        while r < n and cul_sum < s:
            r += 1
            cul_sum = cum[r] - cum[l]

        if cul_sum >= s:
            length = r - l
            min_length = min(length, min_length)
        l += 1

    print(min_length)