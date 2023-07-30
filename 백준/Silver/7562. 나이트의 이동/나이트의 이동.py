import sys
from collections import deque

input = sys.stdin.readline

tc = int(input().strip())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(sx, sy, ex, ey, visited):
    if (sx, sy) == (ex, ey):
        return 0

    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()
        if (x, y) == (ex, ey):
            return visited[x][y] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= I or ny < 0 or ny >= I:
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


for _ in range(tc):
    I = int(input().strip())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    visited = [[0] * I for _ in range(I)]
    print(bfs(sx, sy, ex, ey, visited))
