def destroy_by_magic(d, s):
    cx = cy = N // 2
    for i in range(1, s + 1):
        nx = cx + dx[d] * i
        ny = cy + dy[d] * i
        mat[nx][ny] = 0


def convert_to_line():
    global line_size
    ddx = [0, 1, 0, -1]
    ddy = [-1, 0, 1, 0]
    line_size = 0
    cx = cy = N // 2
    d = 0
    loop_count = 2
    for dist in range(1, N):
        if dist == N - 1:
            loop_count = 3
        for i in range(loop_count):
            for j in range(dist):
                cx += ddx[d]
                cy += ddy[d]
                if mat[cx][cy] != 0:
                    line[line_size] = mat[cx][cy]
                    line_size += 1
            d = (d + 1) % 4


def destroy_by_rule():
    global line_size
    global ret
    point = 0
    count = 1
    for i in range(1, line_size):
        if line[i - 1] == line[i]:
            count += 1
        else:
            if count >= 4:
                for j in range(1, count + 1):
                    point += line[i - j]
                    line[i - j] = 0
            count = 1
    if count >= 4:
        for j in range(1, count + 1):
            point += line[line_size - j]
            line[line_size - j] = 0

    ret += point
    return point


def remove_zero():
    global line_size
    back = [0] * 2500
    back_size = 0
    for i in range(line_size):
        if line[i] != 0:
            back[back_size] = line[i]
            back_size += 1

    for i in range(back_size):
        line[i] = back[i]
    line_size = back_size


def change_by_rule():
    global line_size
    back_size = 0
    back = [0] * 2500
    count = 1
    for i in range(1, line_size):
        if line[i - 1] == line[i]:
            count += 1
        else:
            if back_size < N * N - 2:
                back[back_size] = count
                back[back_size + 1] = line[i - 1]
                back_size += 2
            count = 1

    # line_size = 0 인 경우, 구슬을 확대할 수 없는 경우
    if line_size > 0 and back_size < N * N - 2:
        back[back_size] = count
        back_size += 1
        back[back_size] = line[line_size - 1]
        back_size += 1

    for i in range(back_size):
        line[i] = back[i]

    line_size = back_size


def convert_to_mat():
    global line_size
    ddx = [0, 1, 0, -1]
    ddy = [-1, 0, 1, 0]

    cx = cy = N // 2
    d = 0
    loop_count = 2
    cur = 0
    for dist in range(1, N):
        if dist == N - 1:
            loop_count = 3
        for i in range(loop_count):
            for j in range(dist):
                cx += ddx[d]
                cy += ddy[d]
                # if mat[cx][cy] != 0:
                #     line[line_size] = mat[cx][cy]
                #     line_size += 1
                if cur < line_size:
                    mat[cx][cy] = line[cur]
                    cur += 1
                else:
                    mat[cx][cy] = 0
            d = (d + 1) % 4


N, M = map(int, input().split())
ret = 0
mat = [list(map(int, input().split())) for _ in range(N)]

line = [0] * 2500
line_size = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(M):
    d, s = map(int, input().split())
    # d 인덱스가 1부터 시작하기 때문에 1 빼기
    destroy_by_magic(d - 1, s)
    convert_to_line()
    while destroy_by_rule() != 0:
        remove_zero()
    remove_zero()
    change_by_rule()
    convert_to_mat()

print(ret)
