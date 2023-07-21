import sys

input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n

min_cost = int(1e9)


def dfs(start, now, cost):
    if sum(visited) == n:
        if arr[now][start]:
            global min_cost
            min_cost = min(cost + arr[now][start], min_cost)
        return

    for i in range(n):
        if not visited[i]:
            if arr[now][i]:
                visited[i] = 1
                dfs(start, i, cost + arr[now][i])
                visited[i] = 0


for i in range(n):
    visited[i] = 1
    dfs(i, i, 0)
    visited[i] = 0

print(min_cost)

