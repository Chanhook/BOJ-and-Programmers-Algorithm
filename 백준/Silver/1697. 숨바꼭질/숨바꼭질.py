from collections import deque

n, k = map(int, input().split())

MAX = 100001
dist = [0] * MAX


def bfs(n, k):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            return
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)


bfs(n, k)
