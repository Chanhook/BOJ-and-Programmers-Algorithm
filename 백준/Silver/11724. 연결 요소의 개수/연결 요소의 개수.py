import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)

visited = [0] * n
result = 0


def bfs(x):
    visited[x] = 1
    q = deque()
    q.append(x)

    while q:
        node = q.popleft()

        for next_node in arr[node]:
            if not visited[next_node]:
                visited[next_node] = 1
                q.append(next_node)

    return 1


for i in range(n):
    if not visited[i]:
        result += bfs(i)

print(result)
