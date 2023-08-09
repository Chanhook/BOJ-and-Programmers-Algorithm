from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

coins = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            coins.append((i, j))

coin1_loc, coin2_loc = coins


def in_board(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(coin1_loc, coin2_loc):
    q = deque([(coin1_loc, coin2_loc, 0)])

    while q:
        coin1, coin2, cur_cnt = q.popleft()
        if cur_cnt == 10:
            return -1
        for i in range(4):
            nx1, ny1 = coin1[0] + dx[i], coin1[1] + dy[i]
            nx2, ny2 = coin2[0] + dx[i], coin2[1] + dy[i]
            if in_board(nx1, ny1) and in_board(nx2, ny2):
                if board[nx1][ny1] == '#':
                    nx1, ny1 = coin1[0], coin1[1]
                if board[nx2][ny2] == '#':
                    nx2, ny2 = coin2[0], coin2[1]
                q.append(((nx1, ny1), (nx2, ny2), cur_cnt + 1))
            elif (in_board(nx1, ny1) and not in_board(nx2, ny2)) or \
                    (not in_board(nx1, ny1) and in_board(nx2, ny2)):
                return cur_cnt + 1
    

print(bfs(coin1_loc, coin2_loc))
