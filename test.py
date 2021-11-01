import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**8)
from collections import deque

def dfs(x,y,count):
    global K,ans
    visit[x][y]=True
    if x==H-1 and y==W-1:
        ans=min(ans,count)
        return
    if K>0:
        for i in range(12):
            mx=x+kdx[i]
            my=y+kdy[i]
            if 0<=mx<H and 0<=my<W:
                if visit[mx][my]==False and grid[mx][my]==0: 
                    visit[mx][my]=True
                    dfs(mx,my,count+1)
                    K-=1
                    visit[mx][my]=False
    else:
        for i in range(8,12):
            mx=x+kdx[i]
            my=y+kdy[i]
            if 0<=mx<H and 0<=my<W:
                if visit[mx][my]==False and grid[mx][my]==0:
                    visit[mx][my]=True
                    dfs(mx,my,count+1)
                    K-=1
                    visit[mx][my]=False


def bfs(x,y,count):
    global K,ans
    q=deque()
    q.append((x,y,count))
    while q:
        a,b,c=q.popleft()
        visit[a][b]=True
        if a==H-1 and b==W-1:
            ans=min(c,ans)
            break
        if K>0:
            for i in range(12):
                mx=a+kdx[i]
                my=b+kdy[i]
                if 0<=mx<H and 0<=my<W:
                    if visit[mx][my]==False and grid[mx][my]==0: 
                        visit[mx][my]=True
                        q.append((mx,my,c+1))
                        K-=1
                        visit[mx][my]=False
        else:
            for i in range(8,12):
                mx=a+kdx[i]
                my=b+kdy[i]
                if 0<=mx<H and 0<=my<W:
                    if visit[mx][my]==False and grid[mx][my]==0:
                        visit[mx][my]=True
                        q.append((mx,my,c+1))
                        visit[mx][my]=False



if __name__=="__main__":
    K=int(input())
    W,H=map(int,input().split())
    grid=list(list(map(int,input().split())) for _ in range(H))
    visit=[[False]*W for _ in range(H)]
    kdx=[-1, -2, -2, -1, 1, 2,  2,  1,    0,0,1,-1]
    kdy=[-2, -1,  1,  2, 2, 1, -1, -2,    1,-1,0,0]
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    ans=sys.maxsize
    bfs(0,0,0)

    if ans==sys.maxsize:
        print(-1)
    else:
        print(ans)