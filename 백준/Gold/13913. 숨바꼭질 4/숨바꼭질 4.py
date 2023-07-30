from collections import deque


def path(x):
    arr = []
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = move[temp]
    arr.reverse()
    print(*arr)


def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x + 1, x - 1, 2 * x):
            if 0 <= i < MAX and dist[i] == 0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x


N, K = map(int, input().split())
MAX = 100001
dist = [0] * MAX
move = [0] * MAX
bfs()