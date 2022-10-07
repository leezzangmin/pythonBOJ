import sys;input=sys.stdin.readline
from collections import deque
K=int(input())
W,H=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(H)]
#visit=list([False]*W for _ in range(H))
for i in range(H):
    for j in range(W):
        if grid[i][j]==1:
            grid[i][j]=-1
        else:
            grid[i][j]=int(1e9)

dx=[0,0,1,-1,  -1,-2,-2,-1,1, 2,  2,  1]
dy=[1,-1,0,0,  -2,-1, 1,2 ,2, 1, -1, -2]

Q=deque()
Q.append((0,0,K))
grid[0][0]=0
while Q:
    x,y,coin=Q.popleft()
   # visit[x][y]=True
 #   print(x,y,'xy')
    if coin>0:
        for i in range(4,12):
            mx=x+dx[i]
            my=y+dy[i]
            if 0<=mx<H and 0<=my<W and grid[mx][my]!=-1:# and visit[mx][my]==False:
                if grid[mx][my]>grid[x][y]+1:
                    grid[mx][my]=grid[x][y]+1
                   # visit[mx][my]=True
                    Q.append((mx,my,coin-1))
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if 0<=mx<H and 0<=my<W and grid[mx][my]!=-1:# and visit[mx][my]==False:
                if grid[mx][my]>grid[x][y]+1:
                    grid[mx][my]=grid[x][y]+1
                    Q.append((mx,my,coin))
    else:
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            
            if 0<=mx<H and 0<=my<W and grid[mx][my]!=-1:# and visit[mx][my]==False:
                if grid[mx][my]>grid[x][y]+1:
                    grid[mx][my]=grid[x][y]+1
                    #visit[mx][my]=True
                    Q.append((mx,my,coin))
    for i in grid:
        print(i)
    print()

if grid[H-1][W-1]==int(1e9):
    print(-1)
else:
    print(grid[H-1][W-1])

#print(ans)