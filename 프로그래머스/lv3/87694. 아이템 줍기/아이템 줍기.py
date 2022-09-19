from collections import deque

def pprint(graph):
    for rows in graph:
        print(*rows)
    
def solution(rectangle, characterX, characterY, itemX, itemY):
    nrow = 51 * 2
    ncol = 51 * 2
    graph = [[0 for _ in range(ncol)] for __ in range(nrow)]
    visit = [[0 for _ in range(ncol)] for __ in range(nrow)]
    
    del_rectangle=[]
    
    for rect in rectangle*2:
        x1,y1,x2,y2 = rect
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        
        del_x1 = x1 + 1
        del_y1 = y1 + 1
        del_x2 = x2 - 1
        del_y2 = y2 - 1
        
        del_rectangle.append([del_x1, del_y1, del_x2, del_y2])
        
        for i in range(y2-y1+1):
            graph[y1+i] = graph[y1+i][:x1]+[1]*(x2-x1+1)+graph[y1+i][x2+1:]
    
    for rect in del_rectangle:
        x1,y1,x2,y2 = rect
        
        for i in range(y2-y1+1):
            graph[y1+i] = graph[y1+i][:x1]+[0]*(x2-x1+1)+graph[y1+i][x2+1:]
                
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

        
    def dfs(x,y,target_i,target_j):
        q = deque()
        q.append((x,y))
        visit[x][y] = 1
        
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx<0 or nx >=nrow or ny<0 or ny>=ncol:
                    continue
                if graph[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    q.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
                
                if nx == target_i and ny == target_j:
                    return graph[nx][ny]
            
            
    return dfs(characterY*2, characterX*2,itemY*2,itemX*2) //2
