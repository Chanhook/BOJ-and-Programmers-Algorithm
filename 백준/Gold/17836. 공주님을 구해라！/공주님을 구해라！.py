from collections import deque
import sys

N, M, T = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, graph, visit, N, M, T):
    q = deque()
    q.append((x, y))
    visit[x][y] = 1

    sword_time = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0 and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))
                continue
            if graph[nx][ny] == 2 and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                sword_time = visit[nx][ny]-1 + (N-1 - nx) + (M-1 - ny)
                continue

    if sword_time and visit[N-1][M-1] != 0:
        total_time = min(sword_time, visit[N-1][M-1] - 1)
    elif not sword_time and visit[N-1][M-1] != 0:
        total_time = visit[N-1][M-1]
    elif sword_time and visit[N-1][M-1] == 0:
        total_time = sword_time
    elif not sword_time and visit[N-1][M-1] == 0:
        return "Fail"

    if total_time > T:
        return "Fail"
    else:
        return total_time


print(bfs(0, 0, graph, visit, N, M, T))
