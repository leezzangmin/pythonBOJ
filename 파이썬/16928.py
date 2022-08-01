import sys;input=sys.stdin.readline;sys.setrecursionlimit(10**7);from collections import deque
grid = [i for i in range(0,101)]
dp=[1000]*101
dp[1]=0
visit=[False]*101
N,M=map(int,input().split())

for _ in range(N+M):
    a,b=map(int,input().split())
    grid[a]=b

def dfs():
    Q=deque()
    Q.append((1,1))
    while Q:
        x,origin = Q.popleft()
        visit[x]=True
        for i in range(1,7):
            mx=x+i
            if 0<mx<101 and visit[mx]==False:
                visit[mx]=True
                dp[mx]=min(dp[mx],dp[x]+1,dp[origin]+1)
                Q.append((grid[mx],mx))

    
dfs()
print(dp[100])