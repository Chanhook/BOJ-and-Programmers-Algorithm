from collections import deque
def solution(numbers, target):
    answer = 0
    size = len(numbers)
    next_idx = 1
    
    q = deque()
    q.append([numbers[0], next_idx])
    q.append([-numbers[0], next_idx])
    
    while q:
        cur_num, cur_next_idx = q.popleft()
        if cur_next_idx == size:
            if cur_num == target:
                answer += 1
            continue
        
        next_num1 = cur_num + numbers[cur_next_idx]
        next_num2 = cur_num - numbers[cur_next_idx]
        
        q.append([next_num1, cur_next_idx+1])
        q.append([next_num2, cur_next_idx+1])
    
    return answer