def bfs():
    Q=deque()
    Q.append((0,0))
    while Q:
        x,y=Q.popleft()
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if 0<=mx<X and 0<=my<Y and grid[mx][my]==0 and air[mx][my]==False:
                air[mx][my]=True
                Q.append((mx,my))


def dfs(x,y):
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if 0<=mx<X and 0<=my<Y:
            if air[mx][my]==True:
                grid[x][y]=0
                return
def check():
    global cheese
    cheese=0
    for i in range(X):
        for j in range(Y):
            if grid[i][j]==1:
                cheese+=1
    return cheese

            
from collections import deque
import sys;input=sys.stdin.readline;sys.setrecursionlimit(10**8)
X,Y=map(int,input().split())
grid=list( list(map(int,input().split())) for _ in range(X)     )

# 접촉부분
dx=[0,0,1,-1]
dy=[1,-1,0,0]

count=0
c=[check()]
while c[-1]!=0:
    air=list( list([False]*Y) for _ in range(X))
    bfs()
    for i in range(X):
        for j in range(Y):
            if air[i][j]==False and grid[i][j]==1:
                dfs(i,j)

    count+=1
    c.append(check())
print(count)
try:
    print(c[-2])
except:
    print(c[-1])