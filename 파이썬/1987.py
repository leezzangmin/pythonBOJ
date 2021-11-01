import sys;from collections import deque
input=sys.stdin.readline

def bfs():
    s=[]
    while q:
        x,y=q.popleft()
        s.append(grid[x][y])
        for i in range(4):
            mx=x+dx[i]
            my=y+dy[i]
            if 0<=mx<R and 0<=my<C:
                if visit[mx][my]==False and grid[mx][my] not in s:
                    visit[mx][my]=True
                    q.append((mx,my))
                    visit[mx][my]=False

#백트래킹은 dfs라고 합니다



if __name__=="__main__":
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    R,C=map(int,input().split())
    grid=list(  input().rstrip()  for _ in range(R))
    visit=[[False]*C for _ in range(R)]
    q=deque()
    q.append((0,0))
    bfs()
