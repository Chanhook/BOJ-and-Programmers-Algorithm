import sys

cubes = [
    [[0, 1, 0, 0],
     [1, 1, 1, 1],
     [0, 1, 0, 0]],
    [[1, 0, 0, 0],
     [1, 1, 1, 1],
     [1, 0, 0, 0]],
    [[0, 1, 0, 0],
     [1, 1, 1, 1],
     [1, 0, 0, 0]],
    [[0, 0, 1, 0],
     [1, 1, 1, 1],
     [1, 0, 0, 0]],
    [[0, 0, 0, 1],
     [1, 1, 1, 1],
     [1, 0, 0, 0]],
    [[0, 0, 1, 0],
     [1, 1, 1, 1],
     [0, 1, 0, 0]],
    [[0, 0, 1, 1, 1],
     [1, 1, 1, 0, 0]],
    [[0, 0, 1, 1],
     [0, 1, 1, 0],
     [1, 1, 0, 0]],
    [[0, 0, 1, 1],
     [1, 1, 1, 0],
     [1, 0, 0, 0]],
    [[1, 1, 0, 0],
     [0, 1, 1, 1],
     [0, 1, 0, 0]],
    [[0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 0, 1, 1]]
]


# 시계 방향 90 회전
def rotate(arr):
    n = len(arr)
    m = len(arr[0])
    rotated_arr = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            rotated_arr[j][n - i - 1] = arr[i][j]
    return rotated_arr


# 뒤집기
def flip(arr):
    return arr[::-1]


def check(board, cube, x, y):
    for i in range(len(cube)):
        for j in range(len(cube[0])):
            nx = x + i
            ny = y + j
            if 0 <= nx < len(board) and 0 <= ny < len(board):
                if board[nx][ny] != cube[i][j]:
                    return False
            else:
                return False
    return True


input = sys.stdin.readline
for _ in range(3):
    a = []
    for _ in range(6):
        a.append(list(map(int, input().split())))
    ans = False
    for cube in cubes:
        # 큐브당 상하반전
        for mir in range(2):
            cube = flip(cube)
            # 큐브당 90도 회전 
            for rot in range(4):
                cube = rotate(cube)
                for x in range(6):
                    for y in range(6):
                        ans |= check(a, cube, x, y)
    print("yes" if ans else "no")