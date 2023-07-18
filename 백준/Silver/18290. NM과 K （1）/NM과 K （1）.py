import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_sum = -1e9


def find(sx, sy, cnt, total):
    if cnt == k:
        global max_sum
        max_sum = max(max_sum, total)
        return

    for x in range(sx, n):
        for y in range(sy if x == sx else 0, m):
            if visited[x][y]:
                continue

            is_neigh = False
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny]:
                        is_neigh = True
                        break

            if not is_neigh:
                visited[x][y] = 1
                find(x, y, cnt + 1, total + board[x][y])
                visited[x][y] = 0


find(0, 0, 0, 0)
print(max_sum)
