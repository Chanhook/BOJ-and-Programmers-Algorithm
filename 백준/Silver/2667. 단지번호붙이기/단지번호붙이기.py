import sys
from _collections import deque
def bfs(x,y):
    cnt=1
    q=deque()
    q.append((x,y))
    visit[x][y]=True
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny] and not visit[nx][ny]:
                visit[nx][ny]=True
                q.append((nx,ny))
                cnt+=1
    return cnt
n=int(sys.stdin.readline())
graph=[]
for i in range(n):
    graph.extend([[int(x) for x in y]for y in sys.stdin.readline().split()])

visit=[[False for _ in range(n)]for x in range(n)]
#print(visit)

dx=[-1,0,1,0]
dy=[0,1,0,-1]

house=[]
for i in range(n):
    for j in range(n):
        if graph[i][j] and not visit[i][j]:
            house.append(bfs(i,j))
house.sort()
print(len(house))
for h in house:
    print(h)
