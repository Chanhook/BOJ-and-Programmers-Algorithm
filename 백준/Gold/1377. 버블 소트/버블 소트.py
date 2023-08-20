import sys

input = sys.stdin.readline
n = int(input().strip())
arr = []
for i in range(n):
    arr.append([int(input().strip()), i])

sorted_arr = sorted(arr)
answer = []

for i in range(n):
    answer.append(sorted_arr[i][1] - arr[i][1])

print(max(answer) + 1)
