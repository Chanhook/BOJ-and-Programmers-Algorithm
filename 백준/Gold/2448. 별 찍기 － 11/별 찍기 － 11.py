def recursive(n, x, y, board):
    if n == 3:
        for i in range(3):
            for j in range(5):
                if i == 0:
                    if j == 2:
                        board[x + i][y + j] = '*'
                elif i == 1:
                    if j % 2 == 1:
                        board[x + i][y + j] = '*'
                else:
                    board[x + i][y + j] = '*'
    else:
        recursive(n // 2, x, y + (n // 2), board)
        recursive(n // 2, x + (n // 2), y, board)
        recursive(n // 2, x + (n // 2), y + n, board)


n = int(input())
board = [[' '] * (6 * (n // 3) - 1) for _ in range(n)]
recursive(n, 0, 0, board)
for i in range(n):
    print(''.join(board[i]))
