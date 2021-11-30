import sys;input=sys.stdin.readline
from collections import deque
M,N,H=map(int,input().split())
tomato=[]
for _ in range(H):
    temp=[]
    for i in range(N):
        temp.append(list(map(int,input().split())))
    tomato.append(temp)# 1은 익은 토마토, 0은 안익은 토마토, -1은 빈칸


dx=[0,0,-1,1,0,0]
dy=[1,-1,0,0,0,0]
dz=[0,0,0,0,1,-1]

def check(): # 시작할때 다 익어있음
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if tomato[z][x][y]==0:
                    return False
    return True

def bfs():
    while Q:
        z,x,y=Q.popleft()
        for i in range(6):
            mx=x+dx[i]
            my=y+dy[i]
            mz=z+dz[i]
            if 0<=mx<N and 0<=my<M and 0<=mz<H and tomato[mz][mx][my]==0:
                tomato[mz][mx][my]=tomato[z][x][y]+1
                Q.append((mz,mx,my))

if check():
    print(0)
else:
    Q=deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k]==1:
                    Q.append((i,j,k))
    bfs()
    if check()==False:
        print(-1)
    else:
        ans=-999
        for i in range(H):
            for j in range(N):
                for k in range(M):
                    ans=max(ans,tomato[i][j][k])
        print(ans-1)
    