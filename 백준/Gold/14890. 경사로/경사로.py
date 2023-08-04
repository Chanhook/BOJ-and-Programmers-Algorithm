import sys

input = sys.stdin.readline
n, l = map(int, input().split())
rarr = [list(map(int, input().split())) for _ in range(n)]
carr = list(zip(*rarr))
result = 0


def pos(line):
    for i in range(1, len(line)):
        # 차이가 1보다 큰 경우
        if abs(line[i] - line[i - 1]) > 1:
            return False

        # 현재 높이 < 이전 높이 -> 오른쪽 탐색
        if line[i] < line[i - 1]:
            for j in range(l):
                # 범위 넘어섬
                # 이미 사용 중
                # 낮은 지점의 칸의 높이가 모두 같지 않음
                if i + j >= n or used[i + j] or line[i] != line[i + j]:
                    return False
                used[i + j] = True
        # 현재 높이 > 이전 높이 -> 왼쪽 탐색
        elif line[i] > line[i - 1]:
            for j in range(l):
                # 범위 넘어섬
                # 이미 사용 중
                # 낮은 지점의 칸의 높이가 모두 같지 않음
                if i - 1 - j < 0 or used[i - 1 - j] or line[i - 1] != line[i - 1 - j]:
                    return False
                used[i - 1 - j] = True
    # 경사로 설치 또는 평평하여 이동 가능한 길
    return True


# 1. 가로 확인
for row in rarr:
    used = [False for _ in range(n)]  # 사용 여부
    if pos(row):  # 현재 확인할 길을 넣어준다.
        result += 1

# 2. 세로 확인
for col in carr:
    used = [False for _ in range(n)]
    if pos(col):
        result += 1

print(result)