def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    
    left = 0
    right = distance
    
    while left <= right:
        mid = (left+right)//2
        min_dst = distance + 1
        current = 0
        remove_cnt = 0
        
        for rock in rocks:
            diff = rock - current
            if diff < mid:
                remove_cnt += 1
            else:
                current = rock
                min_dst = min(min_dst,diff)
        
        if remove_cnt > n:
            right = mid - 1
        else:
            answer = min_dst
            left = mid + 1
    
    return answer