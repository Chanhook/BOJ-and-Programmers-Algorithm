from collections import deque
from itertools import combinations

def solution(n, wires):
    def bfs(x):
        q = deque()
        q.append(x)
        cnt = 1
        while q:
            now_node = q.popleft()
            for next_node in graph[now_node]:
                if not visited[next_node]:
                    visited[next_node] = 1
                    q.append(next_node)
                    cnt += 1
        return cnt
    
    
    
    total = []
    
    for cwires in list(combinations(wires, n-2)):
        graph = [[] for _ in range(n+1)]
        visited = [0 for _ in range(n+1)]
        for n1,n2 in cwires:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        result = []
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = 1
                cnt = bfs(i)
                result.append(cnt)
        
        total.append(abs(result[0]-result[1]))
        
    return min(total)