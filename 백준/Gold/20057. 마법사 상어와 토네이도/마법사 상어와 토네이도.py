def wind(cx, cy, cd):
    sand = arr[cx][cy]
    # 모든 모래가 이동 후 남은 모래 없음
    arr[cx][cy] = 0

    # 흩어진 모래 총합
    total_sand = 0
    # 격자 밖으로 나간 모래
    left = 0

    for i in range(10):
        nx = cx + torX[cd][i]
        ny = cy + torY[cd][i]

        if i == 9:
            # a에 들어갈 값
            scattered = sand - total_sand
        else:
            scattered = int(sand * rate[i])
            total_sand += scattered

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            left += scattered
        else:
            arr[nx][ny] += scattered

    return left


def solve():
    ret = 0
    cx = cy = N // 2

    visited = [[0] * N for _ in range(N)]
    cd = -1
    while cx != 0 or cy != 0:
        # 여기서 방문처리해줘야한다
        visited[cx][cy] = 1
        nd = (cd + 1) % 4

        nx = cx + dx[nd]
        ny = cy + dy[nd]

        if visited[nx][ny]:
            nd = cd
            # 좌표도 바꿔줘야함
            nx = cx + dx[nd]
            ny = cy + dy[nd]

        ret += wind(nx, ny, nd)

        cx, cy, cd = nx, ny, nd

    return ret


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

torX = [
    (1, -1, 2, -2, 0, 1, -1, 1, -1, 0),
    (-1, -1, 0, 0, 2, 0, 0, 1, 1, 1),
    (1, -1, 2, -2, 0, 1, -1, 1, -1, 0),
    (1, 1, 0, 0, -2, 0, 0, -1, -1, -1)
]

torY = [
    (1, 1, 0, 0, -2, 0, 0, -1, -1, -1),
    (1, -1, 2, -2, 0, 1, -1, 1, -1, 0),
    (-1, -1, 0, 0, 2, 0, 0, 1, 1, 1),
    (1, -1, 2, -2, 0, 1, -1, 1, -1, 0)
]

rate = [
    0.01, 0.01, 0.02, 0.02, 0.05, 0.07, 0.07, 0.1, 0.1, 0
]

ret = solve()
print(ret)
