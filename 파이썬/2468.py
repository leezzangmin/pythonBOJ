import sys;input=sys.stdin.readline;sys.setrecursionlimit(10**8)
N=int(input())
grid=list(list(map(int,input().split())) for _ in range(N))

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dfs(x,y,height):
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if 0<=mx<N and 0<=my<N and visit[mx][my]==False and grid[mx][my]>height:
            visit[mx][my]=True
            dfs(mx,my,height)

maxVal=-1
for i in range(N):
    for j in range(N):
        maxVal=max(maxVal,grid[i][j])

ans=0
for h in range(0, maxVal+1):
    visit=list([False]*N for _ in range(N))
    temp=0
    for i in range(N):
        for j in range(N):
            if visit[i][j]==False and grid[i][j]>h:
                visit[i][j]=True
                dfs(i,j,h)
                temp+=1
    ans=max(ans,temp)
print(ans)