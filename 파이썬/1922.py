import sys;input=sys.stdin.readline
from collections import deque

def dfs(x,y):
    global ans
    grid[x][y]=123
    ans+=1
    for abc in range(4):
        mx=x+dx[abc]
        my=y+dy[abc]
        if 0<=mx<N and 0<=my<M and grid[mx][my]==-1 :
            dfs(mx,my)

N,M,K=map(int,input().split())
grid=[[ 0 for _ in range(M) ] for _ in range(N)]

for _ in range(K):
    a,b=map(int,input().split())
    grid[a-1][b-1]=-1


dx=[0,0,-1,1]
dy=[1,-1,0,0]
gans=-1

for i in range(N):
    for j in range(M):
        if grid[i][j]==-1:
            ans=0
            dfs(i,j)
            gans=max(ans,gans)
print(gans)