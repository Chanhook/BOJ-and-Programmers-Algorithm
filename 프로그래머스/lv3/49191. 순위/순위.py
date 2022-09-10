from collections import deque

def solution(n, results):
    answer = 0
    results.sort()
    win_graph = [[] for i in range(n+1)]
    lose_graph = [[] for i in range(n+1)]
    
    for w,l in results:
        win_graph[w].append(l)
        lose_graph[l].append(w)
    
    def bfs(start):
        win_q = deque()
        win = 0
        win_q.append(start)
        win_visit=[0]*(n+1)
        
        lose_q = deque()
        lose = 0
        lose_q.append(start)
        lose_visit=[0]*(n+1)
        
        while win_q:
            now = win_q.popleft()
            for node in win_graph[now]:
                if not win_visit[node]:
                    win_visit[node] = 1
                    win_q.append(node)
                    win += 1
        
        while lose_q:
            now = lose_q.popleft()
            for node in lose_graph[now]:
                if not lose_visit[node]:
                    lose_visit[node] = 1
                    lose_q.append(node)
                    lose += 1
        if win + lose == n-1:
            return 1
        return 0
    
    for i in range(1,n+1):
        answer += bfs(i)
    
    return answer