import sys

input = sys.stdin.readline
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def rotate():
    carr = []
    for a in arr:
        carr.append(a[:])

    sr, sc, er, ec = 0, 0, N - 1, M - 1
    for depth in range(min(M, N) // 2):
        r, c = sr, sc
        for d in range(4):
            while True:
                nr = r + dx[d]
                nc = c + dy[d]
                if sr <= nr <= er and sc <= nc <= ec:
                    arr[nr][nc] = carr[r][c]
                    r, c = nr, nc
                else:
                    break
        sr += 1
        sc += 1
        er -= 1
        ec -= 1


for _ in range(R):
    rotate()

for a in arr:
    print(*a)