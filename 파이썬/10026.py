import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**8)
from collections import deque

def dfs(x,y,color):
    global count2
    visit[x][y]=True
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if 0<=mx<N and 0<=my<N and visit[mx][my]==False:
            if grid[mx][my]==color:
                dfs(mx,my,color)

def bfs(x,y,color):
    q=deque()
    q.append((x,y))

    while q:
        a,b=q.popleft()
        visit[a][b]=True
        for i in range(4):
            mx=a+dx[i]
            my=b+dy[i]
            if 0<=mx<N and 0<=my<N and visit[mx][my]==False:
                if color=='R':
                    if grid[mx][my]=='R' or grid[mx][my]=='G':
                        q.append((mx,my))
                        visit[mx][my]=True
                elif color=='G':
                    if grid[mx][my]=='G' or grid[mx][my]=='R':
                        q.append((mx,my))
                        visit[mx][my]=True
                else:
                    if grid[mx][my]==color:
                        q.append((mx,my))
                        visit[mx][my]=True


# 빨간색과 초록색의 차이를 거의 느끼지 못한다

if __name__=="__main__":
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    N=int(input())
    grid=list(input().rstrip() for _ in range(N))
    visit=[[False]*N for _ in range(N)]
    
    
    count1=0 
    for i in range(N):
        for j in range(N):
            if visit[i][j]==False:
                dfs(i,j,grid[i][j])
                count1+=1
    
    count2=0    
    visit=[[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j]==False:
                bfs(i,j,grid[i][j])                
                count2+=1
    print(count1,count2)

