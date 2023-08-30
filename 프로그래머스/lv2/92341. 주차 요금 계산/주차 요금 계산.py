import math
from collections import defaultdict


def solution(fees, records):
    answer = []
    base_time, base_rate, unit_time, unit_rate = fees

    park = set()
    park_time = defaultdict(int)
    cum_time = defaultdict(int)
    last_time = 23 * 60 + 59
    for record in records:
        time, car_num, history = record.split()
        ho, mi = map(int, time.split(':'))
        time = ho * 60 + mi

        if car_num not in park:
            park.add(car_num)
            park_time[car_num] = time
        else:
            park.remove(car_num)
            cum_time[car_num] += time - park_time[car_num]
            park_time[car_num] = 0

    while park:
        car = park.pop()
        cum_time[car] += last_time - park_time[car]

    sorted_cum_time = sorted(cum_time.items(), key=lambda x: x[0])
    for num, time in sorted_cum_time:
        if time <= base_time:
            answer.append(base_rate)
        else:
            pay = base_rate + math.ceil((time - base_time) / unit_time) * unit_rate
            answer.append(pay)

    return answer