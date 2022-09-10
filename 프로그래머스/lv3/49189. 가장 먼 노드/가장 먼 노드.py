from collections import deque

def solution(n, edge):
    edge.sort()
    graph = [[] for i in range(n+1)]
    distance = [0]*(n+1)
    
    
    for e in edge:
        n1,n2 = e
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    
    q = deque()
    q.append(1)
    distance[1] = 1
    
    while q:
        new_node = q.popleft()
        for n in graph[new_node]:
            if distance[n] == 0 :
                distance[n] = distance[new_node]+1
                q.append(n)
    
    max_cnt = max(distance)
    return distance.count(max_cnt)