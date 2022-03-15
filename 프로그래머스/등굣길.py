from collections import deque
import sys
def solution(m, n, puddles):
    grid = list( [0]*m for _ in range(n) )
    dp = list( [0]*m for _ in range(n) )
    m-=1;n-=1;answer=0
    for x,y in puddles:
        grid[x-1][y-1]=sys.maxsize
    for i in grid:
        print(i)
    
    Q=deque()
    Q.append((0,0))
    dx=[0,1]
    dy=[1,0]
    while Q:
        x,y=Q.popleft()
        for i in range(2):
            mx=x+dx[i]
            my=y+dy[i]
            if 0<=mx<=n and 0<=my<=m and grid[mx][my]!=sys.maxsize:
                print('awejhfuiawejfuio')
                grid[mx][my]=grid[x][y]+1
                Q.append((mx,my))

    for i in grid:
        print(i,'asdf')
    answer=grid[n][m]
    return answer%1000000007


print(solution(4,3,[[2,2]]))