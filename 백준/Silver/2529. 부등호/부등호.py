import sys

input = sys.stdin.readline

k = int(input().strip())
symbols = list(input().split())

num = [i for i in range(10)]
visited = [0] * 10

max_num = 0
min_num = int(1e10)


def dfs(idx, string):
    if len(string) == k + 1:
        global max_num
        global min_num
        max_num = max(max_num, int(string))
        min_num = min(min_num, int(string))
        return

    for i in range(10):
        if not visited[i]:
            last_num = string[-1]
            if symbols[idx] == '<':
                if int(last_num) < i:
                    visited[i] = 1
                    dfs(idx + 1, string + str(i))
                    visited[i] = 0
                else:
                    continue
            elif symbols[idx] == '>':
                if int(last_num) > i:
                    visited[i] = 1
                    dfs(idx + 1, string + str(i))
                    visited[i] = 0
                else:
                    continue


for i in range(10):
    visited[i] = 1
    dfs(0, str(i))
    visited[i] = 0

print(max_num if len(str(max_num)) == k + 1 else '0' + str(max_num))
print(min_num if len(str(min_num)) == k + 1 else '0' + str(min_num))
