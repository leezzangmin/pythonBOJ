import sys;input=sys.stdin.readline
from collections import defaultdict
N,K,R=map(int,input().split())
cow_grid=[[0]*N for _ in range(N)]
d=defaultdict()

for _ in range(R):
    x1,y1,x2,y2=map(int,input().split())
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    try:
        d[(x1,y1)].append([x2,y2])
    except:
        d[(x1,y1)]=[[x2,y2]]
    try:
        d[(x2,y2)].append([x1,y1])
    except:
        d[(x2,y2)]=[[x1,y1]]



visit=[[False]*N for _ in range(N)]
for i in range(K):
    cow_x,cow_y=map(int,input().split())
    cow_grid[cow_x-1][cow_y-1]=1
dx=[0,0,1,-1]
dy=[1,-1,0,0]
#print(d,'default')
def dfs(x,y):
    if cow_grid[x][y]==1:
        temp=[[x,y]]
    else:
        temp=[]
    visit[x][y]=True
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if 0<=mx<N and 0<=my<N and visit[mx][my]==False:
            if (x,y) in d.keys():
                if [mx,my] not in d[x,y]:
                    temp+=dfs(mx,my)
            else:
                temp+=dfs(mx,my)
    return temp

result=[]
for i in range(N):
    for j in range(N):
        if cow_grid[i][j]==1 and visit[i][j]==False:
    
            cow_family=dfs(i,j)
    
            result.append(cow_family)

if len(result)==1:
    print(0)
else:
    answer=0
    for i in range(len(result)):
        for j in range(i+1,len(result)):
            answer+=(len(result[i])*len(result[j]))
    print(answer)
