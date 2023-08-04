import sys
from collections import deque

input = sys.stdin.readline

t = int(input().strip())
wheels = [deque(map(int, list(input().strip()))) for _ in range(t)]
k = int(input().strip())
rotates = [list(map(int, input().split())) for _ in range(k)]

for now_t, clockwise, in rotates:
    pos_turn = [[0] * 2 for _ in range(t)]
    pos_turn[now_t - 1] = [1, clockwise]

    temp = -clockwise
    for i in range(now_t, t):
        if wheels[i][6] == wheels[i - 1][2]:
            break
        else:
            pos_turn[i] = [1, temp]
            temp *= -1

    temp = -clockwise
    for i in range(now_t - 1, 0, -1):
        if wheels[i][6] == wheels[i - 1][2]:
            break
        else:
            pos_turn[i - 1] = [1, temp]
            temp *= -1

    for i in range(t):
        if pos_turn[i][0] == 0:
            continue

        if pos_turn[i][1] == 1:
            wheels[i].appendleft(wheels[i].pop())
        elif pos_turn[i][1] == -1:
            wheels[i].append(wheels[i].popleft())

result = 0
for row in wheels:
    if row[0] == 1:
        result += 1

print(result)
