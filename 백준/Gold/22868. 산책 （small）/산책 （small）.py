import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for idx in range(1, N+1):
    graph[idx].sort()

s, e = map(int, sys.stdin.readline().split())


def get_adj_node(visit, q, cur_node, cur_cnt):
    for next in graph[cur_node]:
        if visit[next] == -1:
            visit[next] = cur_node
            q.append((next, cur_cnt+1))   # 출발점 제외 경로 리턴, 출발점은 재방문 해야하기 때문에


def go_bfs(start, end, visit, start_cnt) -> list:
    q = deque()
    q.append((start, start_cnt))
    while q:
        cur_node, cur_cnt = q.popleft()
        # if cur_node == end and start_cnt == 0:
        #     break
        get_adj_node(visit, q, cur_node, cur_cnt)

    path = [end]
    next = visit[end]
    while next != 0:
        path.append(next)
        next = visit[next]
# [-1,0,1,1,2]
#[4,2]
    return path[:-1]


def back_bfs(start, end, visit, start_cnt) -> int:
    q = deque()
    q.append((start, start_cnt))
    while q:
        cur_node, cur_cnt = q.popleft()
        if cur_node == end:
            return cur_cnt
        get_adj_node(visit, q, cur_node, cur_cnt)


visited = [-1]*(N+1)
visited[s] = 0
path = go_bfs(s, e, visited, 0)

visited = [-1]*(N+1)
for idx in path:    # 이미 방문한 경로 표시
    visited[idx] = 1
cnt = back_bfs(e, s, visited, len(path))
print(cnt)
