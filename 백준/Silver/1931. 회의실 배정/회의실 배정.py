from os import times_result
import sys

N = int(sys.stdin.readline().strip())

times = []
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    times += [[s, e]]

times.sort(key=lambda x: (x[1], x[0]))

s, e = times[0]
cnt = 1
for time in times[1:]:
    ns, ne = time
    if e <= ns:
        s, e = ns, ne
        cnt += 1
    else:
        continue

print(cnt)

"""
반례
2
1 1
0 1

x[1]로만 정렬했기 때문에
[[1,1],[0,1]]로 들어가기 때문에
2가 아닌 1로 나왔다.
"""
