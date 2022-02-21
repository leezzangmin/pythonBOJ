import sys;input=sys.stdin.readline
from collections import deque
N,M=map(int,input().split())
grid=list( list(map(int,input().split())) for _ in range(N) )

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(a,b):
    visit =[ [False]*M for _ in range(N) ]
    visit2=[ [False]*M for _ in range(N) ]
    Q=deque()
    Q.append((a,b))
    Q2=deque()
    while Q:
        x,y=Q.popleft()
        visit[x][y]=True
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if 0<=mx<N and 0<=my<M and visit[mx][my]==False:
                if grid[mx][my]==0:
                    visit[mx][my]=True
                    Q.append((mx,my))

                else:
                    if visit2[mx][my]==True:
                        visit[mx][my]=True
                        Q2.append((mx,my))
                    else:
                        visit2[mx][my]=True
    while Q2:
        x,y=Q2.popleft()
        grid[x][y]=0

def isEmpty():
    for i in range(N):
        for j in range(M):
            if grid[i][j]==1:
                return False
    return True

ans=0
while isEmpty()==False:

    bfs(0,0)
    ans+=1
print(ans)
