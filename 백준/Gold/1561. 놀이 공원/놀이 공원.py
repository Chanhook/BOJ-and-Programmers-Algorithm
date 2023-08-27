n, m = map(int, input().split())
arr = list(map(int, input().split()))

if n <= m:
    print(n)
else:
    time, lo, hi, = 0, 0, int(6e10)
    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = m  # 최초 비어있는 놀이기구에 m명 먼저 태움
        for i in range(m):
            cnt += mid // arr[i]
        if cnt >= n:
            time = mid
            hi = mid - 1
        else:
            lo = mid + 1

    ride_cnt = m
    for i in range(m):
        ride_cnt += (time - 1) // arr[i]

    for i in range(m):
        if time % arr[i] == 0:
            ride_cnt += 1
        if ride_cnt == n:
            print(i + 1)
            break