n = int(input().strip())
board = [0] * n
answer = 0


def promising(idx):
    for i in range(idx):
        if board[i] == board[idx] or idx - i == abs(board[i] - board[idx]):
            return False
    return True


def nqueen(idx):
    if idx == n:
        global answer
        answer += 1
        return

    for i in range(n):
        board[idx] = i
        if promising(idx):
            nqueen(idx + 1)


nqueen(0)
print(answer)