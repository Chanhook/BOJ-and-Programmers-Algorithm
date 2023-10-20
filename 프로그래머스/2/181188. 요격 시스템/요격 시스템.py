def solution(targets):
    answer = 1
    targets.sort(key = lambda x: x[1])
    last_end = targets[0][1]
    for s, e in targets[1:]:
        if last_end <= s:
            last_end = e
            answer += 1

    
    return answer