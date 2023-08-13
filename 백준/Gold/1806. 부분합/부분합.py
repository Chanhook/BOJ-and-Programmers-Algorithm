import sys

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = n
if sum(arr) < s:
    print(0)
else:
    l, r = 0, 0
    total = 0
    while r < n:
        total += arr[r]
        while total >= s:
            ans = min(r - l + 1, ans)
            total -= arr[l]
            l += 1
        r += 1
    print(ans)
