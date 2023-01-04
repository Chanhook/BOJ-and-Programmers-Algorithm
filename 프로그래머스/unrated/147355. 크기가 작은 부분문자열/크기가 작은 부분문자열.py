def solution(t, p):
    answer = 0
    
    p_len = len(p)
    p_num = int(p)
    
    for i in range(len(t)):
        partial_str = t[i:i+p_len]
        if len(partial_str) == p_len and int(partial_str) <= int(p):
            answer += 1
        
        
        
    
    return answer