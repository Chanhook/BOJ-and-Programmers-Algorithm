import sys
from collections import deque

input = sys.stdin.readline
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def rotate():
    q = deque()
    for depth in range(min(N, M) // 2):
        r = c = depth

        for d in range(4):  # 큐에 담아놓고
            while True:
                nr = r + dx[d]
                nc = c + dy[d]
                if depth <= nr < N - depth and depth <= nc < M - depth:
                    q.append(arr[r][c])
                    r = nr
                    c = nc
                else:
                    break

        # 돌린다
        for _ in range(R % ((N - depth * 2) * 2 + (M - depth * 2) * 2 - 4)):
            q.appendleft(q.pop())

        for d in range(4):  # 큐에서 돌린 값을 넣는다
            while True:
                nr = r + dx[d]
                nc = c + dy[d]
                if depth <= nr < N - depth and depth <= nc < M - depth:
                    arr[r][c] = q.popleft()
                    r = nr
                    c = nc
                else:
                    break


rotate()

for a in arr:
    print(*a)