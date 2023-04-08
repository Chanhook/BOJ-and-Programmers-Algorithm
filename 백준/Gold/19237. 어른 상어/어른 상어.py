def smell():
    for i in range(M):
        cx, cy = shark_pos[i]
        MAP[cx][cy][1] = K


def move():
    for m in range(M):
        # 쫓겨난게 존재한다면
        if shark_pos[m] == 0:
            continue

        flag = False
        cx, cy = shark_pos[m]
        cd = directions[m]

        # 인접칸 중 아무 냄새 없는 칸
        count = 0
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if MAP[nx][ny] == 0:
                count += 1

        # 아무 냄새 없는 칸이 있다면
        # 현재 방향에서 우선순위로
        if count != 0:
            for d in priorities[m][cd - 1]:
                nx = cx + dx[d - 1]
                ny = cy + dy[d - 1]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if MAP[nx][ny] == 0:
                    shark_pos[m] = [nx, ny]
                    directions[m] = d
                    flag = True
                    break

        if flag:
            continue

        # 자신의 냄새가 있는 칸으로
        count = 0
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if MAP[nx][ny][0] == m:
                count += 1

        # 자신의 냄새 칸이 있다면
        if count != 0:
            for d in priorities[m][cd - 1]:
                nx = cx + dx[d - 1]
                ny = cy + dy[d - 1]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if MAP[nx][ny][0] == m:
                    shark_pos[m] = [nx, ny]
                    directions[m] = d
                    flag = True
                    break
        if flag:
            continue


def update_smell():
    for x in range(N):
        for y in range(N):
            if MAP[x][y] != 0:
                MAP[x][y][1] -= 1
                if MAP[x][y][1] == 0:
                    MAP[x][y] = 0

    for m in range(M):
        # 쫓겨난게 존재한다면
        if shark_pos[m] == 0:
            continue
        cx, cy = shark_pos[m]
        if MAP[cx][cy] == 0:
            MAP[cx][cy] = [m, K]
        else:
            cur_shark_num = MAP[cx][cy][0]
            my_shark_num = m
            # 자기 번호와 같다면
            if cur_shark_num == my_shark_num:
                MAP[cx][cy] = [my_shark_num, K]
            # 다르고, 기존 번호가 낮다면
            elif cur_shark_num < my_shark_num:
                shark_pos[my_shark_num] = 0
            # 다르고 내 번호가 낮다면
            else:
                shark_pos[cur_shark_num] = 0
                MAP[cx][cy] = [my_shark_num, K]


def check_sharks():
    for shark in shark_pos[1:]:
        if shark != 0:
            return False
    return True


def solve():
    time = 0
    smell()

    while True:
        time += 1
        move()
        update_smell()

        if check_sharks():
            return print(time)

        if time >= 1000:
            return print(-1)


N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

# 해당 상어 넘버의 위치
## Idx 0 = 상어 1
shark_pos = [0] * M

for x in range(N):
    for y in range(N):
        if MAP[x][y]:
            shark_pos[MAP[x][y] - 1] = [x, y]
            MAP[x][y] = [MAP[x][y] - 1, 0]

# idx 0 = 위 1
directions = list(map(int, input().split()))

# u d l r
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

priorities = []

for m in range(M):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    priorities.append(temp)

solve()
