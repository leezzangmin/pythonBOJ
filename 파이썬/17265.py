import sys
N=int(input())
grid=list(input().split() for _ in range(N))
from collections import deque
#visit

dx=[0,1]
dy=[1,0]
def bfs():
    maxans=-sys.maxsize
    minans=sys.maxsize
    Q=deque()
    Q.append((0,0,int(grid[0][0]),""))
    while Q:
        x,y,value,giho=Q.popleft()
        if x==N-1 and y==N-1:
            maxans=max(maxans,value)
            minans=min(minans,value)
            continue
        for i in range(2):
            mx=x+dx[i]
            my=y+dy[i]
            if 0<=mx<N and 0<=my<N:
                flag=True
                try:
                    int(grid[mx][my])
                except:
                    flag=False
                if flag:#grid[mx][my].isdigit():
                    if giho=='*':
                        mvalue=value*int(grid[mx][my])
                    elif giho=='-':
                        mvalue=value-int(grid[mx][my])
                    elif giho=='+':
                        mvalue=value+int(grid[mx][my])
                    else:
                        print('error')
                        exit()
                    Q.append((mx,my,mvalue,""))
                else: # 기호
                    Q.append((mx,my,value,grid[mx][my]))

    return maxans,minans

    

print(*bfs())
