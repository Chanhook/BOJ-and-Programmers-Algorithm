from collections import deque
from copy import deepcopy


def calc_point():
    point = 0
    max_area = []
    max_rainbow = 0
    for color in range(1, M + 1):
        # 무지개 블럭 때문에 매번 갱신한다
        # 1번도 밟을 수 있고, 2번도 밟을 수 있기 때문
        visited = [[0] * N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if not visited[x][y] and board[x][y] == color:
                    q = deque()
                    area = []
                    rainbow = 0

                    q.append([x, y])
                    area.append([x, y])
                    visited[x][y] = 1

                    while q:
                        cx, cy = q.popleft()
                        for d in range(4):
                            nx = cx + dx[d]
                            ny = cy + dy[d]
                            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                                continue
                            if not visited[nx][ny] and (board[nx][ny] == color or board[nx][ny] == 0):
                                q.append([nx, ny])
                                area.append([nx, ny])
                                visited[nx][ny] = 1
                                if board[nx][ny] == 0:
                                    rainbow += 1
                    if (len(max_area) < len(area)) or (len(max_area) == len(area) and max_rainbow < rainbow) or (
                            len(max_area) == len(area) and max_rainbow == rainbow and max_area[0] < area[0]):
                        max_area = deepcopy(area)
                        max_rainbow = rainbow

    if len(max_area) >= 2:
        point = len(max_area) * len(max_area)
        for i in range(len(max_area)):
            x, y = max_area[i]
            # 블록 삭제
            board[x][y] = -2

    return point


def gravity():
    for y in range(N):
        blank = 0
        for x in range(N - 1, -1, -1):
            if board[x][y] == -2:
                blank += 1
            elif board[x][y] == -1:
                blank = 0
            else:
                if blank != 0:
                    board[x + blank][y] = board[x][y]
                    board[x][y] = -2


def rotate_left():
    n = len(board)
    rotated_board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_board[n - j - 1][i] = board[i][j]

    for i in range(n):
        for j in range(n):
            board[i][j] = rotated_board[i][j]


def solve():
    point = 0
    cur_point = 0
    while True:
        cur_point = calc_point()
        point += cur_point
        gravity()
        rotate_left()
        gravity()
        if cur_point == 0:
            break

    return point


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

ret = solve()
print(ret)
