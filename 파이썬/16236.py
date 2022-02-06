# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 
# 나머지 칸은 모두 지나갈 수 있다.
# 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 
# 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

# 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
#    거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
#   거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
import sys;input=sys.stdin.readline
from collections import deque
N=int(input())
space = list(list(map(int,input().split())) for _ in range(N))

for i in range(N):
    for j in range(N):
        if space[i][j]==9:
            babyLocation=[i,j]

babySize = 2
babyEat = 0
time = 0

def findNearestAndEatable():
    index=0
    count=0
    distance=sys.maxsize
    for i,j,d in fishList:

        tempDist = d
        if tempDist==distance:
            if fishList[index][0]>i:
                index=count
            elif fishList[index][0]==i and fishList[index][1]>j:
                index=count
                
        elif tempDist<distance:
            distance=tempDist
            index=count

        count+=1
    if distance == sys.maxsize:
        return -1
    else:
        return index
 
def bfs():
    fishList=[]
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    visit=list([False]*N for _ in range(N))

    Q=deque()
    Q.append((babyLocation[0],babyLocation[1],0))
    while Q:
        
        x,y,d = Q.popleft() 
        visit[x][y]=True
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if 0<=mx<N and 0<=my<N and visit[mx][my]==False and 0<=space[mx][my]<=babySize:
                visit[mx][my]=True
                Q.append((mx,my,d+1))
                if 1<=space[mx][my]<babySize:
                    fishList.append((mx,my,d+1))
                
    return fishList


fishList=bfs()
#sys.exit()
while fishList:
    a = findNearestAndEatable()
    if a!=-1:
        space[babyLocation[0]][babyLocation[1]]=0
        x,y,d=fishList.pop( a )
        time+=d
        babyLocation=[x,y]
        space[x][y] = 0
        babyEat+=1
    else:
        break

    if babySize==babyEat:
        babySize+=1
        babyEat=0
    fishList=bfs()

print(time)