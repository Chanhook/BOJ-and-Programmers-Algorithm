# 토네이도 회전 방향
# 방향별 모래 비율 위치
# a값과 격자 밖의 모래의 양
def recount(x, y, direction):
    if y < 0:
        return

    total = 0
    for dx, dy, z in direction:
        nx = x + dx
        ny = y + dy
        if z == 0:  # a
            new_sand = sand[x][y] - total
        else:
            new_sand = int(sand[x][y] * z)
            total += new_sand

        if 0 <= nx < N and 0 <= ny < N:
            sand[nx][ny] += new_sand
        else:
            ans[0] += new_sand
            
    sand[x][y] = 0


N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]

left = [
    (1, 1, 0.01),
    (-1, 1, 0.01),
    (1, 0, 0.07),
    (-1, 0, 0.07),
    (2, 0, 0.02),
    (-2, 0, 0.02),
    (1, -1, 0.1),
    (-1, -1, 0.1),
    (0, -2, 0.05),
    (0, -1, 0),
]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]

s_x = s_y = N // 2
ans = [0]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 토네이도 회전 방향
tor_dir_dic = {0: left, 1: down, 2: right, 3: up}
time = 0

for i in range(2 * N - 1):
    d = i % 4
    if d == 0 or d == 2:
        time += 1
    for _ in range(time):
        n_x = s_x + dx[d]
        n_y = s_y + dy[d]
        recount(n_x, n_y, tor_dir_dic[d])  # y좌표, 방향
        s_x, s_y = n_x, n_y

print(ans[0])
