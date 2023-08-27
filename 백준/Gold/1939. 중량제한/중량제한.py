from collections import deque
import sys


def bfs(weight, start, end):
    q = deque()
    q.append(start)
    visit = [0] * (n + 1)
    visit[start] = 1
    while q:
        now = q.popleft()
        for next, next_weight in graph[now]:
            if not visit[next] and next_weight >= weight:
                visit[next] = 1
                q.append(next)

    if visit[end]:
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
    if bfs(mid, island1, island2):
        res = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(res)
