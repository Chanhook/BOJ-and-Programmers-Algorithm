import sys

input = sys.stdin.readline
cnt = [0, 0, 0]

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]


def conquer(x, y, n):
    lst = [paper[i][y:y + n] for i in range(x, x + n)]
    k = set(sum(lst, []))
    if len(k) == 1:
        cnt[k.pop()] += 1
        return

    d = n // 3
    for i in range(0, n, d):
        for j in range(0, n, d):
            conquer(x + i, y + j, d)


conquer(0, 0, N)
print(cnt[-1])
print(cnt[0])
print(cnt[1])
