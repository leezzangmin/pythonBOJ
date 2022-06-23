import sys;input=sys.stdin.readline;import math;sys.setrecursionlimit(10**8)
N,L,R=map(int,input().split())
nations=[list(map(int,input().split())) for _ in range(N)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def move(x,y):
    global a
    a.append((x,y))
    visit[x][y]=True
    for abcd in range(4):
        mx=x+dx[abcd]
        my=y+dy[abcd]
        if 0<=mx<N and 0<=my<N and visit[mx][my]==False and L<=abs(nations[x][y]-nations[mx][my]) and R>=abs(nations[x][y]-nations[mx][my]):
            move(mx,my)


is_move=True
ans=0
while is_move==True:
    is_move=False
    visit=[[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j]==False:
                a=list()
                move(i,j)
                if len(a)!=1:
                    temp=0
                    is_move=True
                    for ab,cd in a:
                        temp+=nations[ab][cd]
                    move_count=math.floor(temp/len(a))
                    for ab,cd in a:
                        nations[ab][cd]=move_count
    if is_move:
        ans+=1

print(ans)