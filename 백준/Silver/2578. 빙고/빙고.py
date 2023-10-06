import sys

input = sys.stdin.readline
n = 5
bingo = [list(map(int, input().split())) for _ in range(n)]
checked = [[0] * n for _ in range(n)]
nums = [list(map(int, input().split())) for _ in range(n)]
nums = sum(nums, [])

dic = dict()
for i in range(n):
    for j in range(n):
        dic[bingo[i][j]] = (i, j)


def get_bingo():
    bingo_cnt = 0
    for row in checked:
        if sum(row) == 5:
            bingo_cnt += 1

    for col in zip(*checked):
        if sum(col) == 5:
            bingo_cnt += 1

    s = 0
    for i in range(n):
        s += checked[i][i]

    if s == 5:
        bingo_cnt += 1

    s = 0
    for i in range(n):
        s += checked[n - i - 1][i]

    if s == 5:
        bingo_cnt += 1

    return bingo_cnt


round = 0
for i, num, in enumerate(nums):
    round += 1
    x, y = dic[num]
    checked[x][y] = 1
    bingo_cnt = get_bingo()
    if bingo_cnt >= 3:
        break

print(round)
