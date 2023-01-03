def solution(storey):
    answer = 0
    tmp = 0

    while (storey):
        if storey % 10 == 5:
            tmp = storey//10
            if tmp % 10 >= 5:
                answer += 5
                storey += 5
            else:
                answer += 5
        elif storey % 10 > 5:
            answer += 10 - (storey % 10)
            storey += 10
        elif storey % 10 < 5:
            answer += storey % 10

        storey //= 10

    return answer

