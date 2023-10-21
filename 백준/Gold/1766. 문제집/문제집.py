import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort(indegree):
    result = []
    heap = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            heappush(heap, (indegree[i], i))

    while heap:
        _, now = heappop(heap)
        result.append(now)

        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                heappush(heap, (indegree[next], next))

    return result


result = topology_sort(indegree)
print(*result)
