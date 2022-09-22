import sys;input=sys.stdin.readline
from collections import deque
from itertools import combinations
import copy
N,M=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

virus=[]
for i in range(N):
    for j in range(N):
        if grid[i][j]==2:
            grid[i][j]=0
            virus.append((i,j))
        elif grid[i][j]==1:
            grid[i][j]=-2


c=combinations(virus,M)
ans=int(1e9)
for i in c:

    visit=list([False]*N for _ in range(N))
    gg=copy.deepcopy(grid)

    Q=deque(i)

    for x1,y1 in Q:
        gg[x1][y1]=0
        visit[x1][y1]=True

    while Q:
        x,y=Q.popleft()
        visit[x][y]=True
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if 0<=mx<N and 0<=my<N and visit[mx][my]==False and gg[mx][my]==0:
                gg[mx][my]=gg[x][y]+1
                Q.append((mx,my))

    temp=-1
    flag=False
    for i in range(N):
        if flag:
            break
        for j in range(N):
            if gg[i][j]==0 and visit[i][j]==False:
                flag=True
                break
            temp=max(temp,gg[i][j])
    if not flag:
        ans=min(ans,temp)

if ans==int(1e9):
    print(-1)
else:
    print(ans)


# 5 2
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 2 2