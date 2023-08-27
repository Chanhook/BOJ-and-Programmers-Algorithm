def is_exist(mid, k):
    cur_cnt = 0

    for i in range(1, n + 1):
        cur_cnt += min(mid // i, n)

    if cur_cnt >= k:
        return True
    return False


n = int(input())
k = int(input())
lo, hi = 1, k
while lo < hi:
    mid = lo + (hi - lo) // 2
    if is_exist(mid, k):
        hi = mid
    else:
        lo = mid + 1

print(lo)
