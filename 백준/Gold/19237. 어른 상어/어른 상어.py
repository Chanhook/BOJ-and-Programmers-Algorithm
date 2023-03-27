n, m, k = map(int, input().split())

# 모든 상어의 위치와 방향 정보를 포함
graph = [list(map(int, input().split())) for _ in range(n)]

# 모든 상어의 현재 방향 정보
directions = list(map(int, input().split()))

# 각 위치마다 [특정 상어 번호, 특정 상어 냄새의 남은 시간] 을 저장하는 2차원리스트
smell = [[[0, 0]] * n for _ in range(n)]

# 각 상어의 방향 우선순위 정보
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

# 특정 위치에서 이동 가능한 4가지 방향 (상 하 좌 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 모든 냄새 정보 업데이트
def update_smell():
    for i in range(n):
        for j in range(n):
            # 냄새가 존재하면 1 만큼 감소
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어가 존재하는 위치의 냄새를 k로 설정
            if graph[i][j]:
                smell[i][j] = [graph[i][j], k]


def move():
    # 이동 결과를 담기 위한 임시 array
    new_array = [[0] * n for _ in range(n)]
    # 각 위치를 하나씩 확인
    for x in range(n):
        for y in range(n):
            # 상어가 존재하는 경우
            if graph[x][y]:
                # 현재 상어의 번호
                shark_num = graph[x][y]
                # 현재 상어의 방향
                direction = directions[shark_num - 1]
                # 갈 수 있는 방향부터 리스팅
                # 냄새가 없는 방향부터 찾기
                # 냄새가 없는 방향이 없을 경우
                found = False
                for i in range(4):
                    nx = x + dx[priorities[shark_num - 1][direction - 1][i] - 1]
                    ny = y + dy[priorities[shark_num - 1][direction - 1][i] - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        # 냄새가 없다면
                        if smell[nx][ny][1] == 0:
                            # 해당 상어의 방향 이동시키기
                            directions[shark_num - 1] = priorities[shark_num - 1][direction - 1][i]
                            # 상어 이동시키기 (만약 이미 다른 상어가 있다면 번호가 낮은 것이 들어가도록)
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = shark_num
                            else:
                                new_array[nx][ny] = min(shark_num, new_array[nx][ny])
                            found = True
                            break
                if found:
                    continue
                # 주변에 모두 냄새가 남아있다면, 자신의 냄새가 있는 곳으로 이동
                for i in range(4):
                    nx = x + dx[priorities[shark_num - 1][direction - 1][i] - 1]
                    ny = y + dy[priorities[shark_num - 1][direction - 1][i] - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        # 자신의 냄새라면
                        if smell[nx][ny][0] == shark_num:
                            # 해당 상어의 방향 이동시키기
                            directions[shark_num - 1] = priorities[shark_num - 1][direction - 1][i]
                            # 상어 이동시키기
                            new_array[nx][ny] = shark_num
                            break
    return new_array


time = 0
while True:
    # 모든 위치 업데이트
    update_smell()
    graph = move()
    time += 1

    # 1번 상어만 남았는지 확인
    check = True
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 1:
                check = False
    if check:
        print(time)
        break

    # time이 1000초를 지났는지 확인
    if time >= 1000:
        print(-1)
        break
