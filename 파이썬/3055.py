# 비어있는 곳은 '.'로 표시되어 있고, 물이 차있는 지역은 '*', 돌은 'X'
# 비버의 굴은 'D'로, 고슴도치의 위치는 'S'로 나타내어져 있다.

import sys;input=sys.stdin.readline
from collections import deque
R,C=map(int,input().split())
grid=[list(input().rstrip()) for _ in range(R)]
visit=[[False] * C for _ in range(R)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
waterQ=deque()
sonicQ=deque()
for i in range(R):
    for j in range(C):
        if grid[i][j]=="*":
            waterQ.append((i,j))
            visit[i][j]=True
        elif grid[i][j]=="S":
            sonicQ.append((i,j))
            visit[i][j]=True

minute=0
while sonicQ:
    for _ in range(len(waterQ)):
        x,y=waterQ.popleft()
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if 0<=mx<R and 0<=my<C and visit[mx][my]==False and grid[mx][my]=='.':
                waterQ.append((mx,my))
                grid[mx][my]='*'
                visit[mx][my]=True

    
    minute+=1
    for _ in range(len(sonicQ)):
        x,y=sonicQ.popleft()
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if 0<=mx<R and 0<=my<C and visit[mx][my]==False:
                visit[mx][my]=True
                if grid[mx][my]=='D':
                    print(minute)
                    sys.exit()
                if grid[mx][my]=='.':
                    sonicQ.append((mx,my))
print("KAKTUS")

