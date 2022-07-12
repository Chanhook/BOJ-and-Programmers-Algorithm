import sys

n, m = map(int, sys.stdin.readline().split())

graph = {i: set() for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].add(v)
    graph[v].add(u)

# print(graph)


visit = [0] * (n + 1)


def dfs(graph, i):
    visit[i] = 1
    for i in graph[i]:
        if not visit[i]:
            dfs(graph, i)


cnt = 0
for i in range(1, n + 1):
    if not visit[i]:
        dfs(graph, i)
        cnt += 1

print(cnt)
