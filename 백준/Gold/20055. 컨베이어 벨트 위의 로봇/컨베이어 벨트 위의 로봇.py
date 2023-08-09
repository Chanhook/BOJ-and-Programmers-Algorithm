import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
conveyor_belts = deque(list(map(int, input().split())))
size = len(conveyor_belts)
robots = deque([0 for _ in range(size)])
step = 0


def count():
    cnt = 0
    for i in range(size):
        if conveyor_belts[i] == 0:
            cnt += 1
    return cnt


while True:
    step += 1
    # belt, 로봇 회전
    conveyor_belts.appendleft(conveyor_belts.pop())
    robots.appendleft(robots.pop())
    # 내리는 위치
    robots[size // 2 - 1] = 0

    # 이동
    for i in range(size - 1, -1, -1):
        if robots[i] != 1:
            continue
        # 내리는 위치
        nx = (i + 1) % size
        if not robots[nx] and conveyor_belts[nx] >= 1:
            conveyor_belts[nx] -= 1
            robots[nx], robots[i] = robots[i], robots[nx]
        if nx == size // 2 - 1:
            robots[nx] = 0

    # 올리기
    if conveyor_belts[0] > 0 and not robots[0]:
        conveyor_belts[0] -= 1
        robots[0] = 1

    if count() >= k:
        break

print(step)
