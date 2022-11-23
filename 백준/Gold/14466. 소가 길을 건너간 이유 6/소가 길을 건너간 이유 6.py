'''
각각의 소에서 다리를 건너지 않고 다른 소들을 방문할 수 있나?

'''
from collections import deque
import sys

n, k, r = map(int, sys.stdin.readline().split())
paths = dict()
for _ in range(r):
    r, c, nr, nc = map(int, sys.stdin.readline().split())
    paths[(r, c, nr, nc)] = 0
cows = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

cows.sort()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or nx > n or ny < 1 or ny > n:
                continue
            if (x, y, nx, ny) in paths or (nx, ny, x, y) in paths:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))


result = 0
for i, cow in enumerate(cows[:-1]):
    visited = [[0]*(n+1) for _ in range(n+1)]

    r, c = cow
    bfs(r, c)

    left_cows = cows[i+1:]
    for left_cow in left_cows:
        lr, lc = left_cow
        if visited[lr][lc] == 0:
            result += 1

print(result)
