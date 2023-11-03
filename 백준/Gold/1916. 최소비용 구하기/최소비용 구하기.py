import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])

start, end = map(int, input().split())
distance = [int(1e9)] * (n + 1)


def dijkstra(start):
    heap = []
    distance[start] = 0
    heappush(heap, (start, 0))
    while heap:
        now, dist = heappop(heap)
        if dist > distance[now]:
            continue
        for next, d in graph[now]:
            cost = dist + d
            if cost < distance[next]:
                distance[next] = cost
                heappush(heap, (next, cost))


dijkstra(start)
print(distance[end])
