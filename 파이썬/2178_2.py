import sys;input=sys.stdin.readline
from collections import deque
N,M=map(int,input().split())
grid=list(list(input().rstrip()) for _ in range(N))
visit=[[False]*M for _ in range(N)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

Q=deque()
Q.append((0,0,1))
while Q:
    x,y,cost=Q.popleft()
    visit[x][y]=True
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if 0<=mx<N and 0<=my<M and visit[mx][my]==False and grid[mx][my]=='1':
            visit[mx][my]=True
            Q.append((mx,my,cost+1))
            grid[mx][my]=cost+1

print(grid[N-1][M-1])



