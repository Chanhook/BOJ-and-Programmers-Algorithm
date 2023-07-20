import sys

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
visited = [0] * n
max_value = 0

new_arr = []


def dfs():
    if len(new_arr) == n:
        global max_value
        sum_arr = 0
        for i in range(1, n):
            sum_arr += abs(new_arr[i] - new_arr[i - 1])
        max_value = max(max_value, sum_arr)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            new_arr.append(arr[i])
            dfs()
            visited[i] = 0
            new_arr.pop()


for i in range(n):
    visited[i] = 1
    new_arr.append(arr[i])
    dfs()
    visited[i] = 0
    new_arr.pop()

print(max_value)
