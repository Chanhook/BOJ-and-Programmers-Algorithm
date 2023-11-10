def possible(b, mid):
    if len(b) == 1 or '1' not in b or '0' not in b:
        return True

    if b[mid] == '0':
        return False

    left = b[:mid]
    right = b[mid + 1:]
    return possible(left, len(left) // 2) and possible(right, len(right) // 2)


def expressionable_binary_tree(number):
    b = bin(number)[2:]
    cnt = 1
    while 2 ** cnt - 1 < len(b):
        cnt += 1
    while len(b) < 2 ** cnt - 1:
        b = '0' + b

    if possible(b, len(b) // 2):
        return True
    else:
        return False


def solution(numbers):
    answer = [0] * len(numbers)
    for i in range(len(numbers)):
        if expressionable_binary_tree(numbers[i]):
            answer[i] = 1
    return answer