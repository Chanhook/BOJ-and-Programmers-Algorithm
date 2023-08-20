k, n = map(int, input().split())
arr = [int(input().strip()) for _ in range(k)]
arr.sort()

l = 1
r = arr[-1]

while l <= r:
    mid = (l + r) // 2
    count = 0
    for a in arr:
        count += a // mid
    if count < n:
        r = mid - 1
    else:
        l = mid + 1

print(r)
