import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**8)
def dfs(x,y,c):
    global ans
    if c>K:
        return
    if x==0 and y==C-1 and c==K:
        ans+=1
        return    
    visit[x][y]=True

    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if 0<=mx<R and 0<=my<C and h[mx][my]=='.' and not visit[mx][my]:
            dfs(mx,my,c+1)
            visit[mx][my]=False




R,C,K=map(int,input().split())
h=[input().rstrip() for _ in range(R)]
visit=[ [False]*C for _ in range(R)]
ans=0
dx=(0,0,1,-1)
dy=(1,-1,0,0)

dfs(R-1,0,1)
print(ans)