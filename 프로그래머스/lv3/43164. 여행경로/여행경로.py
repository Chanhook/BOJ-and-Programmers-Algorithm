from collections import defaultdict

def solution(tickets):
    answer = []
    
    route = defaultdict(list)
    
    for dptr, arvl in tickets:
        route[dptr].append(arvl)
    
    for k in route.keys():
        route[k].sort(reverse=True)
    
    
    def dfs(dptr):
        stack = [dptr]
        
        while stack:
            arvl = stack.pop()
            if arvl not in route or not route[arvl]:
                answer.append(arvl)
            else:
                stack.append(arvl)
                stack.append(route[arvl].pop())
    
    dfs('ICN')
    
    return answer[::-1]