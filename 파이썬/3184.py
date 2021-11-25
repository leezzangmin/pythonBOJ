import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**8)

R,C=map(int,input().split())
grid=[input().rstrip() for _ in range(R)]
visit=list([False]*C for _ in range(R))

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dfs(x,y):
    visit[x][y]=True
    global lamb
    global wolf
    if grid[x][y]=='v':
        wolf+=1
    elif grid[x][y]=='o':
        lamb+=1
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if 0<=mx<R and 0<=my<C and grid[mx][my]!='#' and visit[mx][my]==False:
            visit[mx][my]=True
            dfs(mx,my)


_wolf,_lamb=0,0
for i in range(R):
    for j in range(C):
        if grid[i][j]!='#' and visit[i][j]==False:
            lamb=0
            wolf=0
            dfs(i,j)
            if lamb>wolf:
                _lamb+=lamb
            else:
                _wolf+=wolf
print(_lamb,_wolf)

