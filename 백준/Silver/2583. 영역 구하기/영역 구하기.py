import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())
graph = [[1]*n for _ in range(m)]
visit = [[0]*n for _ in range(m)]

for i in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i, row in enumerate(graph[y1:y2]):
        for j, col in enumerate(row[x1:x2]):
            graph[i+y1][j+x1] = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    visit[x][y] = 1
    q.append((x, y))
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1 and not visit[nx][ny]:
                visit[nx][ny] = 1
                cnt += 1
                q.append((nx, ny))
    return cnt


result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and not visit[i][j]:
            result.append(bfs(i, j))

print(len(result))
print(*sorted(result))
