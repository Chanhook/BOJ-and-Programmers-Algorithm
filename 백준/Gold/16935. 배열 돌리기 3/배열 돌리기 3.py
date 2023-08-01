import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

operations = list(map(int, input().split()))


def vertical_flip(arr):
    return [a for a in arr[::-1]]


def horizontal_flip(arr):
    return [a[::-1] for a in arr]


def rotate_right_90(arr):
    row = len(arr)
    col = len(arr[0])
    temp = [[0] * row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            temp[j][row - 1 - i] = arr[i][j]
    return temp


def rotate_left_90(arr):
    row = len(arr)
    col = len(arr[0])
    temp = [[0] * row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            temp[col - 1 - j][i] = arr[i][j]
    return temp


def split_quarters(arr, r_mid, c_mid):
    arr1 = []
    arr2 = []
    for a in arr[:r_mid]:
        arr1.append(a[:c_mid])
        arr2.append(a[c_mid:])
    arr3 = []
    arr4 = []
    for a in arr[r_mid:]:
        arr3.append(a[c_mid:])
        arr4.append(a[:c_mid])

    return arr1, arr2, arr3, arr4


def split_quarters_clockwise(arr):
    r_mid = len(arr) // 2
    c_mid = len(arr[0]) // 2
    arr1, arr2, arr3, arr4 = split_quarters(arr, r_mid, c_mid)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i < r_mid:
                if j < c_mid:
                    arr[i][j] = arr4[i][j]
                else:
                    arr[i][j] = arr1[i][j - c_mid]
            else:
                if j < c_mid:
                    arr[i][j] = arr3[i - r_mid][j]
                else:
                    arr[i][j] = arr2[i - r_mid][j - c_mid]

    return arr


def split_quarters_counter_clockwise(arr):
    r_mid = len(arr) // 2
    c_mid = len(arr[0]) // 2
    arr1, arr2, arr3, arr4 = split_quarters(arr, r_mid, c_mid)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i < r_mid:
                if j < c_mid:
                    arr[i][j] = arr2[i][j]
                else:
                    arr[i][j] = arr3[i][j - c_mid]
            else:
                if j < c_mid:
                    arr[i][j] = arr1[i - r_mid][j]
                else:
                    arr[i][j] = arr4[i - r_mid][j - c_mid]

    return arr


for o in operations:
    if o == 1:
        arr = vertical_flip(arr)
    elif o == 2:
        arr = horizontal_flip(arr)
    elif o == 3:
        arr = rotate_right_90(arr)
    elif o == 4:
        arr = rotate_left_90(arr)
    elif o == 5:
        arr = split_quarters_clockwise(arr)
    elif o == 6:
        arr = split_quarters_counter_clockwise(arr)

for a in arr:
    print(*a)