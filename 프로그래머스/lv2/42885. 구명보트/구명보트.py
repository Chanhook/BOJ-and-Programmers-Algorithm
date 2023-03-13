def solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)
    s = 0
    e = len(people)-1
    
    while s <= e:
        if people[s] + people[e] <= limit:
            e -= 1
        s += 1
        answer += 1
    
    return answer