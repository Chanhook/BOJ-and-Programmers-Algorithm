from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    for node in graph[now]:
        if distance[node] == -1:
            distance[node] = distance[now] + 1
            q.append(node)

condition = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        condition = True

if not condition:
    print(-1)
