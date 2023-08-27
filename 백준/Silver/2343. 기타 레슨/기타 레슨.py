n, m, = map(int, input().split())
lectures = list(map(int, input().split()))
if n == m:
    print(max(lectures))
else:
    l = max(lectures)
    ans = r = sum(lectures)

    while l <= r:
        mid = (l + r) // 2
        blu = []
        total = 0
        for lecture in lectures:
            if total + lecture <= mid:
                total += lecture
            else:
                blu.append(total)
                total = lecture
        if total:
            blu.append(total)

        if len(blu) <= m:
            r = mid - 1
            ans = min(max(blu), ans)
        elif len(blu) > m:
            l = mid + 1

    print(ans)
