# 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 
# 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어,
#  그 배추들 역시 해충으로부터 보호받을 수 있다.
#  한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.
# 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 
# 총 몇 마리의 지렁이가 필요한지 알 수 있다. 
# 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.
#  0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)


def dfs(x,y):
    visit[x][y]=True
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if 0<=mx<N and 0<=my<M:
            if visit[mx][my]==False and grid[mx][my]==1:
                dfs(mx,my)

if __name__=="__main__":
    T=int(input())
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for _ in range(T):
        M,N,K=map(int,input().split())
        grid=[ [0]*M for _ in range(N) ]
        visit=[ [False]*M for _ in range(N) ]
        for _ in range(K):
            a,b=map(int,input().split())
            grid[b][a]=1
        count=0
        for i in range(N):
            for j in range(M):
                if visit[i][j]==False and grid[i][j]==1:
                    dfs(i,j)
                    count+=1
        print(count)