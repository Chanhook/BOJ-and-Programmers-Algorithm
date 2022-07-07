import sys

n, c = map(int, sys.stdin.readline().split())
share = []
for i in range(n):
    share.append(int(input()))
share.sort()

min_gap = 1
max_gap = share[-1] - share[0]
result = 0

while min_gap <= max_gap:
    mid = (min_gap + max_gap) // 2
    # 현재 설치된 공유기 위치
    current = share[0]
    count = 1
    for i in range(1, n):
        x = mid + current
        if share[i] >= x:
            # 설치하고 인접 공유기 업데이트
            current = share[i]
            count += 1
    if count >= c:
        min_gap = mid + 1
        result = mid
    else:
        max_gap = mid - 1

print(result)
