from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    total = sum(queue1) + sum(queue2)
    target = (total) // 2
    left_sum = sum(queue1)
    
    if total%2 != 0:
        return -1
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    while q1 and q2:
        if left_sum < target:
            pop_num = q2.popleft()
            q1.append(pop_num)
            left_sum += pop_num
            answer += 1
        elif left_sum > target:
            pop_num = q1.popleft()
            left_sum -= pop_num
            answer += 1
        else:
            return answer
    
    return -1