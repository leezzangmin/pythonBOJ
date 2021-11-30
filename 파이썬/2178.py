import sys;
input=sys.stdin.readline
from collections import deque
def bfs(Q):
    while Q:
        x,y=Q.popleft()
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if 0<=mx<N and 0<=my<M and maze[mx][my]=='1':
                maze[mx][my]=int(maze[x][y])+1
                if mx==N-1 and my==M-1:
                    break
                Q.append((mx,my))
                

dx=(0,0,1,-1)
dy=(1,-1,0,0)
N,M=map(int,input().split())
maze=list(list(input().rstrip()) for _ in range(N))

Q=deque()
Q.append((0,0))
bfs(Q)
print(maze[N-1][M-1])