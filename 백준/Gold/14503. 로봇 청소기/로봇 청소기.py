import sys

input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def find_unclean():
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if board[nr][nc] == 0:
            return True
    return False


answer = 0
while True:
    if board[r][c] == 0:
        board[r][c] = 2
        answer += 1

    if find_unclean():
        for i in range(4):
            d = (d + 3) % 4
            nr = r + dx[d]
            nc = c + dy[d]
            if board[nr][nc] == 0:
                r, c = nr, nc
                break
        continue
    else:
        nd = (d + 2) % 4
        nr = r + dx[nd]
        nc = c + dy[nd]
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] != 1:
            r, c = nr, nc
            continue
        else:
            break

print(answer)