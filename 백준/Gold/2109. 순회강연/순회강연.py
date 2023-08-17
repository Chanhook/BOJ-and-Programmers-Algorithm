import sys

input = sys.stdin.readline
n = int(input().strip())
req = [list(map(int, input().split())) for _ in range(n)]
sorted_req = sorted(req, key=lambda x: -x[0])
schedule = [0] * 10001
ans = 0

if req:
    for i in range(n):
        for j in range(sorted_req[i][1], 0, -1):
            if not schedule[j]:
                schedule[j] = sorted_req[i][0]
                break

    ans = sum(schedule)

print(ans)

