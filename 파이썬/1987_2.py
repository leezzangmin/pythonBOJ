import sys;input=sys.stdin.readline
#from collections import defaultdict
R,C=map(int,input().split())
grid=list(input().rstrip() for _ in range(R))
#visit=list([False]*C for _ in range(R))

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def n(c):
    return ord(c)-65

def dfs(_x,_y,alpha,count):
    global ans
    alpha[n(grid[_x][_y])]=True
    
    for i in range(4):
        mx=_x+dx[i]
        my=_y+dy[i]
        if 0<=mx<R and 0<=my<C and alpha[n(grid[mx][my])]==False:    
            alpha[n(grid[mx][my])]=True
           # visit[mx][my]=True
            dfs(mx,my,alpha,count+1)
            alpha[n(grid[mx][my])]=False
            #visit[mx][my]=False
    ans=max(ans,count)
   
    return ans

#visit[0][0]=True
ans=-sys.maxsize
alphabet=[False]*26
print(dfs(0,0,alphabet,1))
