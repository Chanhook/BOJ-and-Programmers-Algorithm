import math


def get_k_base(k, n):
    res = ''
    while n > 0:
        n, mod = divmod(n, k)
        res += str(mod)
    res = res[::-1]
    return res


def solution(n, k):
    answer = 0
    isPrime = set()
    isNotPrime = set()

    k_base = get_k_base(k, n)
    for str_number in k_base.split('0'):
        if str_number == '':
            continue

        number = int(str_number)
        if number in isPrime:
            answer += 1
            continue
        elif number in isNotPrime or number == 1:
            continue

        isNotP = 0
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                isNotP += 1

        if isNotP:
            isNotPrime.add(number)
        else:
            answer += 1
            isPrime.add(number)

    return answer