import sys
from collections import deque
INF = 1e9

n = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

now_size = 2
now_x, now_y = 0, 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[i][j] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    dist = [[-1]*n for _ in range(n)]
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
            if 0 <= new_x < n and 0 <= new_y < n:
                if dist[new_x][new_y] == -1 and graph[new_x][new_y] <= now_size:
                    dist[new_x][new_y] = dist[x][y] + 1
                    q.append((new_x, new_y))

    return dist

# print(bfs())


def find(dist):
    min_dist = INF
    x, y = 0, 0

    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= graph[i][j] < now_size:
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    x, y = i, j

    if min_dist == INF:
        return None
    else:
        return x, y, min_dist

# print(find(bfs()))


result = 0
ate = 0

while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        x, y, min_dist = value

        ate += 1
        if now_size == ate:
            now_size += 1
            ate = 0

        now_x, now_y = x, y
        result += min_dist
        graph[now_x][now_y] = 0
