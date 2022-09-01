def solution(n, times):
    answer = 0
    times.sort()
    left = 1
    end = n*times[-1]
    
    while left <= end:
        mid = (left + end)//2
        print(f"left: {left}, end: {end}, mid: {mid}")
        process_num = sum(mid//time for time in times)
        print(process_num)
        if process_num >= n:
            end = mid-1
        else:
            left = mid+1
    
    
    return left