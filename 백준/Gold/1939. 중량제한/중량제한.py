from collections import deque
import sys

def bfs2(weight, start, end):
    q = deque()
    q.append((weight, start))
    visited = [0] * (n + 1)
    visited[start] = 1
    while q:
        now_weight, now = q.popleft()
        for next_island, next_weight in graph[now]:
            if not visited[next_island] and next_weight >= weight:
                visited[next_island] = 1
                q.append((next_weight, next_island))
    if visited[end]:
        return True
    else:
        return False


input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

island1, island2 = map(int, input().split())

lo, hi = 1, int(1e9),
res = 0
while lo <= hi:
    mid = lo + (hi - lo) // 2
    if bfs2(mid, island1, island2):
        res = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(res)