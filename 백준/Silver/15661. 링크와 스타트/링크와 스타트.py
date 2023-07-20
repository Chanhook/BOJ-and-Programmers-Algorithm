import sys

input = sys.stdin.readline

n = int(input().strip())
visited = [0] * n
board = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)


def dfs(idx):
    if sum(visited) == n:
        return

    if not (sum(visited) == 0 or sum(visited)) == n:
        global min_diff
        score1, score2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    score1 += board[i][j]
                elif not visited[i] and not visited[j]:
                    score2 += board[i][j]
        min_diff = min(min_diff, abs(score1 - score2))

    for i in range(idx, n):
        visited[i] = 1
        dfs(i + 1)
        visited[i] = 0


dfs(0)
print(min_diff)
