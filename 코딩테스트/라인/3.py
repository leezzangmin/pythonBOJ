from typing import List
from collections import deque;import sys

def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    answer = [[]]
    grid=[[0]*n for _ in range(n)]
    visit=list([False]*n for _ in range(n))

    firedx=[-1,-1,-1,0,0,1,1,1]
    firedy=[-1,0,1,-1,1,-1,0,1]
    icedx=[0,0,1,-1]
    icedy=[1,-1,0,0]

    Q=deque()
    fireQ=deque()
    for x,y in fires:
        x=x-1;y=y-1
        visit[x][y]=True
        Q.append([x,y,0])
        fireQ.append([x,y,0])
    
    i=0
    while Q:
        x,y,time=Q.popleft()
        visit[x][y]=True
        if time==m:
            break
        for i in range(8):
            mx=x+firedx[i]
            my=y+firedy[i]
            if 0<=mx<n and 0<=my<n and visit[mx][my]==False:
                visit[mx][my]=True
                Q.append([mx,my,time+1])
                fireQ.append([mx,my,time+1])
    print(fireQ,'ff',time,x,y)


    maxfire=-sys.maxsize
    for _,_,cost in fireQ:
        maxfire=max(maxfire,cost)
    for x2,y2,cost in fireQ:
        grid[x2][y2]+=(maxfire-cost+1)
    for x,y in fires:
        x=x-1;y=y-1
        grid[x][y]-=1



    print(1)
    for i in grid:
        print(i,'asdf')


    visit=list([False]*n for _ in range(n))
    Q=deque()
    iceQ=deque()
    for x,y in ices:
        x=x-1;y=y-1
        visit[x][y]=True
        Q.append([x,y,0])
        iceQ.append([x,y,0])
    
    i=0
    t=0
    while Q:
        x,y,time=Q.popleft()
        visit[x][y]=True
        if time==m:
            break
        for i in range(4):
            mx=x+icedx[i]
            my=y+icedy[i]
            if 0<=mx<n and 0<=my<n and visit[mx][my]==False:
                visit[mx][my]=True
                Q.append([mx,my,time+1])
                iceQ.append([mx,my,-(time+1)])
    print(iceQ,'iceQ',time,x,y)
    minice=sys.maxsize
    for _,_,cost in iceQ:
        minice=min(minice,cost)

    for x2,y2,cost in iceQ:
        grid[x2][y2]+=(minice-cost-1)

    for x,y in ices:
        x=x-1;y=y-1
        grid[x][y]+=1

    print(2)
    for i in grid:
        print(i,'asdf')




    # 처음부터 다 차있는 경우 edge-case
    return grid


#solution(3,2,[[1,1]],[[3,3]])
solution(5,10,[[5, 5], [1, 3], [5, 2]],[[1, 5], [3, 2]])