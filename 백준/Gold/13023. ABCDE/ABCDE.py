import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()


def find(depth, start, visited):
    if depth == 4:
        return True

    for node in graph[start]:
        if not visited[node]:
            visited[node] = 1
            if find(depth + 1, node, visited):
                return True
            visited[node] = 0

    return False


def go():
    for i in range(n):
        visited[i] = 1
        if find(0, i, visited):
            return True
        visited[i] = 0
    return False


visited = [0] * n
print(1 if go() else 0)
