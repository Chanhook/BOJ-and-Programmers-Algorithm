import sys

input = sys.stdin.readline
n, m = map(int, input().split())

arr1 = [list(map(int, list(input().strip()))) for _ in range(n)]
arr2 = [list(map(int, list(input().strip()))) for _ in range(n)]


def flip_3x3(x, y, arr):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            arr[i][j] ^= 1


ans = 0
for i in range(n):
    for j in range(m):
        if i >= n - 2 or j >= m - 2:
            if arr1[i][j] != arr2[i][j]:
                print(-1)
                exit()

        if arr1[i][j] != arr2[i][j]:
            flip_3x3(i, j, arr1)
            ans += 1

print(ans)
