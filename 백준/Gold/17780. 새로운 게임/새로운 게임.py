import sys

input = sys.stdin.readline
# 우 좌 상 하
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def move(chess_num):
    x, y, z = chess[chess_num]
    # 현재 말이 아래에 있지 않은 경우
    if chess_num != chess_map[x][y][0]:
        return 0

    nx = x + dx[z]
    ny = y + dy[z]

    # 말이 범위를 넘어가거나 파란색을 향하는 경우
    if not 0 <= nx < n or not 0 <= ny < n or board[nx][ny] == 2:
        if 0 <= z <= 1:
            nz = (z+1) % 2
        else:
            nz = (z-1) % 2 + 2
        chess[chess_num][2] = nz
        nx = x + dx[nz]
        ny = y + dy[nz]
        # 여전히 나가거나 파란색일 경우
        if not 0 <= nx < n or not 0 <= ny < n or board[nx][ny] == 2:
            return 0

    chess_set = []
    chess_set.extend(chess_map[x][y])
    chess_map[x][y] = []

    if board[nx][ny] == 1:
        chess_set = chess_set[-1::-1]

    # 새로운 위치로 이동 및 업데이트
    for i in chess_set:
        chess_map[nx][ny].append(i)
        chess[i][:2] = [nx, ny]

    if len(chess_map[nx][ny]) >= 4:
        return 1
    return 0


n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chess_map = [[[] for _ in range(n)] for _ in range(n)]
chess = [0 for _ in range(k)]

for i in range(k):
    x, y, z = map(int, input().split())
    chess_map[x-1][y-1].append(i)
    chess[i] = [x-1, y-1, z-1]

cnt = 1
while cnt <= 1000:
    for i in range(k):
        flag = move(i)
        if flag:
            print(cnt)
            sys.exit()
    cnt += 1
print(-1)
