import sys

input = sys.stdin.readline
n = int(input().strip())
A = list(map(int, list(input().strip())))
B = list(map(int, list(input().strip())))
MAX = int(1e9)
ans = MAX


def change(idx, arr):
    arr[idx - 1] ^= 1
    arr[idx] ^= 1
    if idx < n - 1: arr[idx + 1] ^= 1


def solve(first=False):
    temp = A[:]
    cnt = 0
    if first:
        temp[0] ^= 1
        temp[1] ^= 1
        cnt += 1

    for i in range(1, n):
        if temp[i - 1] != B[i - 1]:
            change(i, temp)
            cnt += 1

    if str(temp) == str(B):
        global ans
        ans = min(cnt, ans)


solve(True)
solve()
print(ans if ans != MAX else -1)

