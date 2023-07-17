import sys

n = int(sys.stdin.readline().strip())
graph = [[a for a in sys.stdin.readline().strip()] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_count = 0


def find_max(graph):
    l = len(graph)
    result = 1
    temp = 1
    for i in range(l):
        for j in range(1, l):
            if graph[i][j] == graph[i][j - 1]:
                temp += 1
            else:
                result = max(result, temp)
                temp = 1

            if j == l - 1:
                result = max(result, temp)
                temp = 1

    for j in range(l):
        for i in range(1, l):
            if graph[i][j] == graph[i - 1][j]:
                temp += 1
            else:
                result = max(result, temp)
                temp = 1

            if i == l - 1:
                result = max(result, temp)
                temp = 1

    return result


for i in range(n):
    for j in range(n):
        cur = graph[i][j]

        for d in range(4):
            ni = i + dx[d]
            nj = j + dy[d]

            if ni < 0 or nj < 0 or ni >= n or nj >= n:
                continue

            neighbor = graph[ni][nj]

            if cur == neighbor:
                continue

            graph[i][j], graph[ni][nj] = graph[ni][nj], graph[i][j]

            result = find_max(graph)
            max_count = max(result, max_count)

            graph[i][j], graph[ni][nj] = graph[ni][nj], graph[i][j]

print(max_count)
