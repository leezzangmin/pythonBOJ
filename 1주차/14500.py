import sys
input=sys.stdin.readline
N,M=map(int,input().split())
grid=list(list(map(int,input().split())) for _ in range(N))
visit=[[0]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans=-sys.maxsize
mv=max(max(*grid))

def dfs(x,y,count,res):
    global ans

    if res + mv * (4-count) <= ans:
        return
    if count==4:
        ans=max(ans,res)
        return
        
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if 0<=mx<N and 0<=my<M and visit[mx][my]==0:
            if count==2:
                visit[mx][my]=1
                dfs(x,y,count+1,res+grid[mx][my])
                visit[mx][my]=0
            visit[mx][my]=1
            dfs(mx,my,count+1,res+grid[mx][my])
            visit[mx][my]=0


for a in range(N):
    for b in range(M):
        visit[a][b]=1
        dfs(a,b,1,grid[a][b])
        visit[a][b]=0
print(ans) 

