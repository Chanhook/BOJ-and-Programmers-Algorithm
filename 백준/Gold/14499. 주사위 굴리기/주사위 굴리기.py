import sys

input = sys.stdin.readline
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]


def turn(dir):
    d1, d2, d3, d4, d5, d6 = dice
    if dir == 1:  # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d4, d2, d1, d6, d5, d3
    elif dir == 2:  # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d3, d2, d6, d1, d5, d4
    elif dir == 3:  # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d5, d1, d3, d4, d6, d2
    elif dir == 4:  # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d2, d6, d3, d4, d1, d5


for i in commands:
    nx = x + dx[i - 1]
    ny = y + dy[i - 1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    turn(i)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[-1]
    else:
        dice[-1] = board[nx][ny]
        board[nx][ny] = 0
    x, y = nx, ny
    print(dice[0])
