'''
시작이 (1,1)이니까 주의해
1번 행과 n번행 연결
비바라기 시전 if n=4
(4,1) (4,2) (3,1) (3,2)

이동을 m번 명령
그 중 i번째 이동 명령은 방향 di 거리 si

그리고 8방향

구름을 이동시키는 함수
구름이 있는 칸에 물을 증가 시키는 함수
    구름의 위치를 반복문으로 순회 물을 증가
구름을 소멸시키는 함수
    back 을 만들어서 기억
(추후 물복사 버그와 구름 생성시 활용을 위해 소멸된 구름위치 기억해야함)
물복사 버그 함수
구름 생성 함수
'''


def create_cloud(x, y):
    global cloud_size
    cloud[cloud_size] = (x, y)
    cloud_size += 1


def init_cloud():
    create_cloud(N - 2, 0)
    create_cloud(N - 1, 0)
    create_cloud(N - 2, 1)
    create_cloud(N - 1, 1)


def move_cloud(d, s):
    global cloud_size
    dist_x = (dx[d] * s) + (N * 50)
    dist_y = (dy[d] * s) + (N * 50)
    for i in range(cloud_size):
        cloud[i] = ((cloud[i][0] + dist_x) % N, (cloud[i][1] + dist_y) % N)


def increase_water():
    global cloud_size
    for i in range(cloud_size):
        x = cloud[i][0]
        y = cloud[i][1]
        arr[x][y] += 1


def delete_cloud():
    global cloud_size
    for i in range(cloud_size):
        x = cloud[i][0]
        y = cloud[i][1]
        cloud_map[x][y] = 1
    cloud_size = 0


def copy_bug():
    backup = []
    for x in range(N):
        for y in range(N):
            if cloud_map[x][y]:
                count = 0
                for d in range(1, 9, 2):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N:
                        count += 1 if arr[nx][ny] else 0
                # 왜냐면 지금 내 행동이 다음 행동에 영향을 직접적으로 줌!
                # 0인데도 복사되서 1로 보이면 count를 1 증가시킬것이기 때문에
                # 증가본에서 찾을 수 있기때문에 논리적으로 조심하자
                # 백업을 둠
                backup.append((x, y, count))
    for x, y, count in backup:
        arr[x][y] += count


def generate_cloud():
    global cloud_size
    for x in range(N):
        for y in range(N):
            if arr[x][y] >= 2 and not cloud_map[x][y]:
                arr[x][y] -= 2
                cloud[cloud_size] = (x, y)
                cloud_size += 1
            if cloud_map[x][y]:
                cloud_map[x][y] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cloud = [0] * 2500
cloud_map = [[0] * N for _ in range(N)]
cloud_size = 0

init_cloud()

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

for i in range(M):
    d, s = map(int, input().split())
    move_cloud(d - 1, s)
    increase_water()
    delete_cloud()
    copy_bug()
    generate_cloud()

ret = 0
for r in arr:
    ret += sum(r)
print(ret)
