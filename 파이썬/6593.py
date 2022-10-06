import sys;input=sys.stdin.readline
from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
dz=[1,-1]
while True:
    L,R,C=map(int,input().split())
    if L==0 and R==0 and C==0:
        break
    d = [[[0]*C for _ in range(R)] for _ in range(L)]
    grid=[]
    for _ in range(L):
        grid.append(list(list(input().rstrip()) for _ in range(R)))
        input()
        
    start=(0,0,0)
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if grid[i][j][k]=='S':
                    start=(j,k,i)
                    
                elif grid[i][j][k]=='E':
                    end=(j,k,i)
                    

    Q=deque()
    Q.append(start)
    while Q:
        x,y,z=Q.popleft()
        cur=d[z][x][y]+1
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if 0<=mx<R and 0<=my<C and grid[z][mx][my]!='#' and d[z][mx][my]==0:
                d[z][mx][my]=cur
                Q.append((mx,my,z))
        for j in range(2):
            mz=z+dz[j]
            if 0<=mz<L and grid[mz][x][y]!='#' and d[mz][x][y]==0:
                d[mz][x][y]=cur
                Q.append((x,y,mz))
    x,y,z=end[0],end[1],end[2]
    if d[z][x][y]==0:
        print('Trapped!')
    else:
        print('Escaped in '+str(d[z][x][y])+' minute(s).')
