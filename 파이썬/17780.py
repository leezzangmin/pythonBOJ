import sys;input=sys.stdin.readline
from collections import deque

# 0은 흰색, 1은 빨간색, 2는 파란색

dx=[0,0,0,-1,1] # 1~5
dy=[0,1,-1,0,0]

N,K=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
commands=[list(map(int,input().split())) for _ in range(K)]

horse=[list([] for _ in range(N)) for _ in range(N)]

for c in range(K):
    x,y,d=commands[c][0],commands[c][1],commands[c][2]
    x-=1;y-=1
    commands[c][0],commands[c][1]=x,y
    horse[x][y].append(c)

turn=0
while turn!=1000:
    turn+=1
    for h in range(K):
        x,y,d=commands[h][0],commands[h][1],commands[h][2]
        if horse[x][y][0]!=h:
            continue
        lh=len(horse[x][y])
        mx=x+dx[d]
        my=y+dy[d]
        if 0<=mx<N and 0<=my<N:
            
            if grid[mx][my]==0:
                horse[mx][my].extend(horse[x][y])
                if len(horse[mx][my])>=4:
                    print(turn)
                    sys.exit()
                for i in range(lh):
                    commands[horse[x][y][i]][0],commands[horse[x][y][i]][1]=mx,my
                horse[x][y]=[]

            elif grid[mx][my]==1:
                horse[mx][my].extend(horse[x][y][::-1])
                if len(horse[mx][my])>=4:
                    print(turn)
                    sys.exit()
                for i in range(lh):
                    commands[horse[x][y][i]][0],commands[horse[x][y][i]][1]=mx,my
                horse[x][y]=[]
                
            elif grid[mx][my]==2:
                mx=x-dx[d]
                my=y-dy[d]
                if 0<=mx<N and 0<=my<N:
                    #if grid[mx][my]==2:
                    if grid[mx][my]==0:
                        horse[mx][my].extend(horse[x][y])
                        if len(horse[mx][my])>=4:
                            print(turn)
                            sys.exit()
                        for i in range(lh):
                            commands[horse[x][y][i]][0],commands[horse[x][y][i]][1]=mx,my
                        horse[x][y]=[]

                    elif grid[mx][my]==1:
                        horse[mx][my].extend(horse[x][y][::-1])
                        if len(horse[mx][my])>=4:
                            print(turn)
                            sys.exit()
                        for i in range(lh):
                            commands[horse[x][y][i]][0],commands[horse[x][y][i]][1]=mx,my
                        horse[x][y]=[]
                    if commands[h][2]==1:
                        commands[h][2]=2
                    elif commands[h][2]==2:
                        commands[h][2]=1
                    elif commands[h][2]==3:
                        commands[h][2]=4
                    elif commands[h][2]==4:
                        commands[h][2]=3

        else: # 범위를 벗어남 - 파란색 취급
            mx=x-dx[d]
            my=y-dy[d]
            if 0<=mx<N and 0<=my<N:
                #if grid[mx][my]==2:

                if grid[mx][my]==0:
                    horse[mx][my].extend(horse[x][y])
                    if len(horse[mx][my])>=4:
                        print(turn)
                        sys.exit()
                    for i in range(lh):
                        commands[horse[x][y][i]][0],commands[horse[x][y][i]][1]=mx,my
                    horse[x][y]=[]


                elif grid[mx][my]==1:
                    horse[mx][my].extend(horse[x][y][::-1])
                    if len(horse[mx][my])>=4:
                        print(turn)
                        sys.exit()
                    for i in range(lh):
                        commands[horse[x][y][i]][0],commands[horse[x][y][i]][1]=mx,my
                    horse[x][y]=[]
                if commands[h][2]==1:
                    commands[h][2]=2
                elif commands[h][2]==2:
                    commands[h][2]=1
                elif commands[h][2]==3:
                    commands[h][2]=4
                elif commands[h][2]==4:
                    commands[h][2]=3


print(-1)