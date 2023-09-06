def check(b):
    length = len(b)
    if length == 1 or '1' not in b or '0' not in b:
        return True

    mid = length // 2
    if b[mid] == '0':
        return False

    left, right = b[:mid], b[mid + 1:]
    return check(left) and check(right)


def is_bt(number):
    b = bin(number)[2:]

    n = 0
    while 2 ** n - 1 < len(b):
        n += 1

    while len(b) < 2 ** n - 1:
        b = '0' + b

    return check(b)


def solution(numbers):
    answer = [0] * len(numbers)
    for i in range(len(numbers)):
        if is_bt(numbers[i]):
            answer[i] = 1
    return answer