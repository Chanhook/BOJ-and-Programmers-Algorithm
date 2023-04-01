import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
fireballs = deque()
for _ in range(m):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireballs.append([r - 1, c - 1, m, s, d])

graph = [[deque() for _ in range(n)] for _ in range(n)]

dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, 1, 1, 1, 0, -1, -1, -1)

for _ in range(k):
    # 모든 파이어볼 이동
    while fireballs:
        cx, cy, cm, cs, cd = fireballs.popleft()
        nx = (cx + cs * dx[cd]) % n
        ny = (cy + cs * dy[cd]) % n
        graph[nx][ny].append([cm, cs, cd])

    for i in range(n):
        for j in range(n):
            # 2개 이상의 파이어볼이 있는 칸
            # 같은 칸 파이어볼 모두 하나로 합침
            if len(graph[i][j]) >= 2:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(graph[i][j])
                while graph[i][j]:
                    _m, _s, _d, = graph[i][j].popleft()
                    sum_m += _m
                    sum_s += _s
                    if _d % 2 == 0:
                        cnt_even += 1
                    else:
                        cnt_odd += 1
                # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0, 2, 4, 6]
                # 아니라면 방향은 1, 3, 5, 7
                else:
                    nd = [1, 3, 5, 7]
                # 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋
                # 질량이 0인 파이어볼은 소멸되어 없어진다.
                if sum_m // 5:
                    for d in nd:
                        fireballs.append([i, j, sum_m // 5, sum_s // cnt, d])

            # 1개 파이어볼
            if len(graph[i][j]) == 1:
                _m, _s, _d = graph[i][j].popleft()
                fireballs.append([i, j, _m, _s, _d])

print(sum(f[2] for f in fireballs))
