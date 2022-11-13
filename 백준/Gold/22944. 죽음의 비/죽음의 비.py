import sys
from collections import deque

N, H, D = map(int, sys.stdin.readline().split())
graph = []

sx = sy = -1
for i in range(N):
    graph.append(list(sys.stdin.readline().strip()))
    for j in range(N):
        if graph[i][j] == 'S':
            sx, sy = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0]*N for _ in range(N)]


def bfs(sx, sy, H, D, visited):
    q = deque()
    q.append((sx, sy, H, 0, 0))
    visited[sx][sy] = 1

    while q:
        x, y, now_h, now_d, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 'E':
                return cnt + 1

            nxt_h = now_h
            nxt_d = now_d

            if graph[nx][ny] == 'U':
                nxt_d = D

            if nxt_d == 0:
                nxt_h -= 1
            else:
                nxt_d -= 1

            if nxt_h == 0:
                continue

            # 예외조건 추가
            if visited[nx][ny] < nxt_h+nxt_d:
                visited[nx][ny] = nxt_h+nxt_d
                q.append((nx, ny, nxt_h, nxt_d, cnt+1))

            # 70% 에서 터짐
            # if not visited[nx][ny]:
            #     visited[nx][ny] = 1
            #     q.append((nx, ny, nxt_h, nxt_d, cnt+1))

    return -1


print(bfs(sx, sy, H, D, visited))