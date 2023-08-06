import sys
from collections import deque

input = sys.stdin.readline
SIZE = 101
board = [[0] * SIZE for _ in range(SIZE)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
dragon_curves = deque()
ans = 0


def make_dragon_curve(cur_y, cur_x, start_direction, generation, cur_generation):
    if cur_generation > generation:
        return

    if cur_generation == 0:
        board[cur_y][cur_x] = 1
        cur_y += dy[start_direction]
        cur_x += dx[start_direction]
        board[cur_y][cur_x] = 1
        dragon_curves.appendleft(start_direction)
        make_dragon_curve(cur_y, cur_x, start_direction, generation, cur_generation + 1)
    else:
        dirs = []
        for i in range(len(dragon_curves)):
            cur_direction = (dragon_curves[i] + 1) % 4
            cur_y += dy[cur_direction]
            cur_x += dx[cur_direction]
            dirs.append(cur_direction)
            board[cur_y][cur_x] = 1

        for d in dirs:
            dragon_curves.appendleft(d)

        make_dragon_curve(cur_y, cur_x, start_direction, generation, cur_generation + 1)


dragon_curve_count = int(input().strip())
for _ in range(dragon_curve_count):
    cur_x, cur_y, start_direction, generation = map(int, input().split())
    make_dragon_curve(cur_y, cur_x, start_direction, generation, 0)
    dragon_curves.clear()

for i in range(SIZE):
    for j in range(SIZE):
        if i + 1 < SIZE and j + 1 < SIZE:
            if board[i][j] == 1 and board[i + 1][j] == 1 and board[i][j + 1] == 1 and board[i + 1][j + 1] == 1:
                ans += 1

print(ans)
