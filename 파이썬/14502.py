import copy
import sys;input=sys.stdin.readline
from itertools import combinations
N,M=map(int,input().split())
grid=list(list(map(int,input().split())) for _ in range(N))

def spread(x,y):
    visit[x][y]=True
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if 0<=mx<N and 0<=my<M and visit[mx][my]==False and temp_grid[mx][my]==0:
            temp_grid[mx][my]=2
            spread(mx,my)

dx=[0,0,1,-1]
dy=[1,-1,0,0]
blank=[]
virus=[]
for i in range(N):
    for j in range(M):
        if grid[i][j]==0:
            blank.append((i,j))
        elif grid[i][j]==2:
            virus.append((i,j))

c=combinations(blank,3)
ans=0

for a,b,c in c:   
    visit=[[False]*M for _ in range(N)]
    temp_grid=copy.deepcopy(grid)
    temp_grid[a[0]][a[1]]=1
    temp_grid[b[0]][b[1]]=1
    temp_grid[c[0]][c[1]]=1
    for aa,bb in virus:
        spread(aa,bb)
    s=0
    for i in temp_grid:
        s+=i.count(0)
    ans=max(ans,s)

print(ans)
