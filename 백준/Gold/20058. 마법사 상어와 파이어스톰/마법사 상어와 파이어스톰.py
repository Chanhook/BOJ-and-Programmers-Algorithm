from collections import deque

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def rotate_and_melting(board, len_board, L):
    new_board = [[0] * len_board for _ in range(len_board)]

    r_size = 2 ** L
    for x in range(0, len_board, r_size):
        for y in range(0, len_board, r_size):
            for i in range(r_size):
                for j in range(r_size):
                    new_board[x + j][y + r_size - i - 1] = board[x + i][y + j]
    board = new_board

    ice_melt = []
    for x in range(len_board):
        for y in range(len_board):
            ice_count = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= len_board or ny < 0 or ny >= len_board:
                    continue
                if board[nx][ny] > 0:
                    ice_count += 1

            if board[x][y] != 0 and ice_count < 3:
                ice_melt.append((x, y))

    for x, y in ice_melt:
        board[x][y] -= 1

    return board


def check_ice_bfs(board, len_board):
    visited = [[0] * len_board for _ in range(len_board)]
    ice_sum = 0
    max_area_count = 0

    for x in range(len_board):
        for y in range(len_board):
            area_count = 0
            if visited[x][y] or board[x][y] == 0:
                continue

            q = deque()
            q.append((x, y))
            visited[x][y] = 1

            while q:
                sx, sy = q.popleft()
                ice_sum += board[sx][sy]
                area_count += 1
                for i in range(4):
                    nx = sx + dx[i]
                    ny = sy + dy[i]
                    if nx < 0 or nx >= len_board or ny < 0 or ny >= len_board:
                        continue

                    if not visited[nx][ny] and board[nx][ny] > 0:
                        q.append((nx, ny))
                        visited[nx][ny] = 1

            max_area_count = max(area_count, max_area_count)

    print(ice_sum)
    print(max_area_count)


def solve():
    N, Q = map(int, input().split())
    len_board = 2 ** N
    board = [list(map(int, input().split())) for _ in range(len_board)]
    L_list = list(map(int, input().split()))

    for L in L_list:
        board = rotate_and_melting(board, len_board, L)

    check_ice_bfs(board, len_board)


solve()
