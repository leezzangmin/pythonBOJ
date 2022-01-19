import sys;input=sys.stdin.readline
from collections import deque


def bfs():
    Q=deque()
    Q.append((0,0))
    grid[0][0]=1
    while Q:
        x,y=Q.popleft()
        visit[x][y]=True
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if 0<=mx<N and 0<=my<M:
                if grid[mx][my]==1:
                    if visit[x][y]==1:
                        continue
                    else:
                        grid[mx][my]=grid[x][y]+1
                        visit[mx][my]=1
                        Q.append((mx,my))
                    
                elif grid[mx][my]==0 or grid[mx][my]>grid[x][y]:
                    grid[mx][my]=grid[x][y]+1
                    visit[mx][my]=visit[x][y]
                    Q.append((mx,my))
                
    for i in grid:
        print(i,'asdf')
    if grid[N-1][M-1]==0:
        print(-1)
    else:
        print(grid[N-1][M-1])




N,M=map(int,input().split())

grid=[list(map(int,input().rstrip())) for _ in range(N)]

visit=[[[0]*2 for _ in range(M)] for _ in range(N)]
for i in visit:
    print(i)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
#bfs()



