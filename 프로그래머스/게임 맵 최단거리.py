from collections import deque
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def solution(maps):
    answer = 0
    N,M=len(maps),len(maps[0])
    for i in range(N):
        for j in range(M):
            if maps[i][j]==0:
                maps[i][j]=False
            if maps[i][j]==1:
                maps[i][j]=10**8
    maps[0][0]=1
    Q=deque()
    Q.append((0,0))
    while Q:
        x,y=Q.popleft()
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if 0<=mx<N and 0<=my<M and maps[mx][my]!=False and maps[x][y]+1<maps[mx][my]:
                maps[mx][my]=maps[x][y]+1
                Q.append((mx,my))

    answer=maps[N-1][M-1]
    if answer==10**8:
        return -1
        
    
    
    return answer