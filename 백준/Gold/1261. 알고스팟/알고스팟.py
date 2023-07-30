import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = 1

    while q:
        x, y, broken = q.popleft()
        if (x, y) == (N - 1, M - 1):
            print(broken)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if not visited[nx][ny]:
                if arr[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny, broken + 1))
                elif arr[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.appendleft((nx, ny, broken))


bfs()