from _collections import deque
import sys

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visit[x][y]=True
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] and not visit[nx][ny]:
                visit[nx][ny]=True
                graph[nx][ny]+=graph[x][y]
                q.append((nx,ny))

    return graph[n-1][m-1]

n, m=map(int,sys.stdin.readline().split())
graph=[]
for i in range(n):
    a=[[int(x) for x in y] for y in sys.stdin.readline().split()]
    graph.extend(a)
visit=[[False for y in range(m)] for x in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(n):
    for j in range(m):
        if graph[i][j] and not visit[i][j]:
            answer=bfs(i,j)

print(answer)