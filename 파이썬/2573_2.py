import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**8)
from collections import deque
N,M=map(int,input().split())
ice=list(list(map(int,input().split())) for _ in range(N))
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x1,y1):
    visit[x1][y1]=True
    Q=deque()
    meltQ=deque()
    Q.append((x1,y1))
    while Q:
        x,y=Q.popleft()
        for k in range(4):
            mx=x+dx[k]
            my=y+dy[k]
            if 0<=mx<N and 0<=my<M:
                if ice[mx][my]>0 and visit[mx][my]==False:
                    visit[mx][my]=True
                    Q.append((mx,my))
                elif ice[mx][my]<=0:
                    meltQ.append((x,y))
    return meltQ

def dfs_count_island(x,y,visit):
    visit[x][y]=True
    for k in range(4):
        mx=x+dx[k]
        my=y+dy[k]
        if 1<=mx<N-1 and 1<=my<M-1 and ice[mx][my]>0 and visit[mx][my]==False:
            dfs_count_island(mx,my,visit)

def one_above_count(iceice):
    for i in range(1,N-1):
        for j in range(1,M-1):
            if iceice[i][j]!=0:
                return True

year=0
#visit=list([False]*M for _ in range(N))
ice_count=0
# for i in range(1,N-1):
#     for j in range(1,M-1):
#         if visit[i][j]==False and ice[i][j]!=0:
#             dfs_count_island(i,j,visit)
#             ice_count+=1

while ice_count<2 and one_above_count(ice):
    ice_count=0
    visit=list([False]*M for _ in range(N))
    for i in range(1,N-1):
        for j in range(1,M-1):
            if visit[i][j]==False and ice[i][j]>0:
                meltQ=bfs(i,j)
                ice_count+=1
                while meltQ:
                    xx,yy=meltQ.popleft()
                    ice[xx][yy]-=1
    #for i in ice:
    #    print(i,'asdf')
#    visit=list([False]*M for _ in range(N))

    # for i in range(1,N-1):
    #     for j in range(1,M-1):
    #         if visit[i][j]==False and ice[i][j]>0:
    #             if ice_count>=2:
    #                 break
    #             dfs_count_island(i,j,visit)
    #             ice_count+=1
    #print(ice_count,'ice_count')
    if ice_count>=2:
        break
    year+=1

if ice_count<2:
    print(0)
else:
    print(year)