import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]

q = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))
            visit[i][j] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue
            elif not visit[nx][ny] and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                visit[nx][ny] = 1
                q.append((nx, ny))


bfs()

answer = 0
for row in graph:
    if 0 in row:
        answer = 0
        break
    answer = max(max(row), answer)

if answer == 1 and sum(sum(visit, [])) == M * N:
    print(0)
else:
    print(answer - 1)
