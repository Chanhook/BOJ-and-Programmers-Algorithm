import math
from collections import defaultdict

def calculate_fee(fees, cumulate_time):
    basic_time, basic_fee, unit_time, unit_fee = fees
    
    if cumulate_time > basic_time:
        return basic_fee + math.ceil((cumulate_time - basic_time)/unit_time) * unit_fee
    
    return basic_fee

def solution(fees, records):
    answer = []
    
    inout_dic = defaultdict(int)
    car_time_dic = defaultdict(list)
    
    for record in records:
        infos = record.split()
        h,m = map(int, infos[0].split(':'))
        car_num = int(infos[1])
        status = infos[2]
        
        if status == 'IN':
            inout_dic[car_num] = 1
            
            if car_time_dic[car_num] == []:
                car_time_dic[car_num].append(h*60 + m)
            else:
                car_time_dic[car_num][0] = h*60 + m
                
        else:
            if inout_dic[car_num] == 1:
                inout_dic[car_num] = 0
            
            out_time = h*60 + m
            in_time = car_time_dic[car_num][0]    
            
            if len(car_time_dic[car_num]) == 1:
                car_time_dic[car_num].append(out_time - in_time)
                car_time_dic[car_num][0] = 0
            else:
                car_time_dic[car_num][0] = 0
                car_time_dic[car_num][1] += out_time-in_time
        
    for car_num, isin in inout_dic.items():
        if isin == 1:
            cur_time = car_time_dic[car_num][0]
            out_time = 23*60 + 59
            
            if len(car_time_dic[car_num]) == 2:
                car_time_dic[car_num][0] = 0
                car_time_dic[car_num][1] += out_time-cur_time
            else:
                car_time_dic[car_num].append(out_time-cur_time)
                car_time_dic[car_num][0] = 0
    
    sorted_car_time_list = sorted(car_time_dic.items(), key = lambda x: x[0])
    
    for car, times in sorted_car_time_list:
        answer.append(calculate_fee(fees, times[1]))
    
    return answer