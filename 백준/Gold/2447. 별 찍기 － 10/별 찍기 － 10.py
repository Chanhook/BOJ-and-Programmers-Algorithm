def recursive(n, x, y, board):
    if n == 1:
        board[0][0] = '*'
        return
    if n == 3:
        for i in range(3):
            for j in range(3):
                board[x + i][y + j] = '*' if i != 1 or j != 1 else ' '
    else:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                recursive(n // 3, x + i * (n // 3), y + j * (n // 3), board)


n = int(input())
board = [[' '] * n for _ in range(n)]
recursive(n, 0, 0, board)
for i in range(n):
    print(''.join(board[i]))
