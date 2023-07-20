import sys

input = sys.stdin.readline

n = int(input().strip())
visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)


def dfs(depth, idx):
    if depth == n // 2:
        global min_diff
        score1, score2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    score1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    score2 += graph[i][j]

        min_diff = min(min_diff, abs(score1 - score2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False


dfs(0, 0)
print(min_diff)