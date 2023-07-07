import sys
from collections import deque


def dfs(graph, start):
    dfs_visited[start] = 1
    print(start, end=' ')

    for n in graph[start]:
        if not dfs_visited[n]:
            dfs(graph, n)


def bfs(graph, start):
    q = deque()
    q.append(start)
    bfs_visited[start] = 1

    while q:
        node = q.popleft()
        print(node, end=" ")

        for n in graph[node]:
            if not bfs_visited[n]:
                q.append(n)
                bfs_visited[n] = 1


n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)

for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(1, n + 1):
    graph[i].sort()

dfs(graph, v)
print()
bfs(graph, v)
