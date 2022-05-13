import sys


def prime(num):
    if num == 1:
        return False
    else:
        for i in range(1, int(num**0.5) + 1):
            if i!=1 and num % i == 0:
                return False
        return True


total = list(range(1, (123456 * 2) + 1))
primes = []

for num in total:
    if prime(num):
        primes += [num]

while True:
    num = int(sys.stdin.readline().rstrip())
    if num==0:
        break
    cnt = 0

    for prime in primes:
        if prime > num and prime <=2*num:
            cnt+=1
        else:
            continue
    print(cnt)

"""
매 입력마다 소수를 생성하는 것은 시간초과
처음에 소수 리스트를 불러와서 계산하자

생각할 점:
1) 모든 입력마다 새로 정보를 생성하는지 살펴보자. 한번만 데이터를 로드 해놓는 경우가 시간초과 안 날 가능성이 있다.
2) 에라토스테네체 복습
"""
