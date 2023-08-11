import sys


def possible(x, y, num):
    # 가로
    if num in board[x]:
        return False

    # 세로
    for i in range(9):
        if num == board[i][y]:
            return False

    # 사각형
    dx, dy = x // 3, y // 3
    for i in range(dx * 3, dx * 3 + 3):
        for j in range(dy * 3, dy * 3 + 3):
            if board[i][j] == num:
                return False

    return True


def sudoku(blank_idx):
    if blank_idx == len(blanks):
        for line in board:
            print(*line)
        sys.exit()

    x, y = blanks[blank_idx]
    for num in range(1, 10):
        if possible(x, y, num):
            board[x][y] = num
            sudoku(blank_idx + 1)
            board[x][y] = 0


input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(9)]
blanks = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
answer = []
sudoku(0)
