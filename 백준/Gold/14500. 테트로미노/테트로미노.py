import sys

input = sys.stdin.readline
tetris = [[(0, 0), (0, 1), (0, 2), (0, 3)],
          [(0, 0), (1, 0), (2, 0), (3, 0)],
          [(0, 0), (1, 0), (0, 1), (1, 1)],
          [(0, 0), (1, 0), (2, 0), (2, 1)],
          [(0, 1), (1, 1), (2, 1), (2, 0)],
          [(0, 0), (0, 1), (1, 1), (2, 1)],
          [(0, 0), (0, 1), (1, 0), (2, 0)],
          [(0, 0), (1, 0), (1, 1), (1, 2)],
          [(0, 2), (1, 1), (1, 2), (1, 0)],
          [(0, 0), (0, 1), (0, 2), (1, 2)],
          [(0, 0), (1, 0), (0, 1), (0, 2)],
          [(0, 0), (1, 0), (1, 1), (2, 1)],
          [(0, 1), (1, 1), (1, 0), (2, 0)],
          [(1, 0), (1, 1), (0, 1), (0, 2)],
          [(0, 0), (0, 1), (1, 1), (1, 2)],
          [(0, 1), (1, 0), (1, 1), (1, 2)],
          [(0, 0), (0, 1), (0, 2), (1, 1)],
          [(0, 0), (1, 0), (1, 1), (2, 0)],
          [(0, 1), (1, 1), (1, 0), (2, 1)]]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def out_of_range_x(N, x1, x2, x3, x4):
    if x1 >= N or x2 >= N or x3 >= N or x4 >= N:
        return True
    return False


def out_of_range_y(M, y1, y2, y3, y4):
    if y1 >= M or y2 >= M or y3 >= M or y4 >= M:
        return True
    return False


max_sum = 0
for tet in tetris:
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = tet

    for i in range(N):
        for j in range(M):
            nx1 = x1 + i
            nx2 = x2 + i
            nx3 = x3 + i
            nx4 = x4 + i

            ny1 = y1 + j
            ny2 = y2 + j
            ny3 = y3 + j
            ny4 = y4 + j

            if out_of_range_x(N, nx1, nx2, nx3, nx4) or out_of_range_y(M, ny1, ny2, ny3, ny4):
                continue

            sum_arr = arr[nx1][ny1] + arr[nx2][ny2] + arr[nx3][ny3] + arr[nx4][ny4]
            max_sum = max(max_sum, sum_arr)

print(max_sum)
