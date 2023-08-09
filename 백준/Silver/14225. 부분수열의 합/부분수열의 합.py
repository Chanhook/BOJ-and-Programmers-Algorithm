from itertools import combinations

n = int(input().strip())
arr = list(map(int, input().split()))

dic = {i: 0 for i in range(1, n * 100000 + 2)}
for i in range(1, n + 1):
    for c in combinations(arr, i):
        sum_sub_arr = sum(c)
        dic[sum_sub_arr] = 1

for i in range(1, n * 100000 + 2):
    if dic[i] == 0:
        print(i)
        break
