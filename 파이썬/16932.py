import sys
input=sys.stdin.readline
N,M=map(int,input().split())
grid=list(list(map(int,input().split())) for _ in range(N))
visit=list([False]*M for _ in range(N))
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y,iii):
    global count
    count+=1
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if 0<=mx<N and 0<=my<M and not visit[mx][my] and grid[mx][my]==1:
            visit[mx][my]=True
            grid[mx][my]=(iii,count)
            dfs(mx,my,iii)
ii=2
for i in range(N):
    for j in range(M):
        if grid[i][j]==1 and visit[i][j]==False:
            count=1
            visit[i][j]=True
            grid[i][j]=(ii,count)
            dfs(i,j,ii)
        ii+=1
print(grid)

## 실패~~~~~~~~~~~