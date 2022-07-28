import sys;input=sys.stdin.readline
N=int(input())
grid=list(list(map(int,input().split())) for _ in range(N))
ans=[0,0,0]#-1 0 1
s=N
visit=[[False]*N for _ in range(N)]

def solve(size,x,y):
    comp=grid[x][y]
    for ii in range(size):
        for jj in range(size):
            if comp!=grid[x+ii][y+jj]:
                return False

    for ii in range(size):
        for jj in range(size):
            visit[x+ii][y+jj]=True

    return True

while s>=1:
    for i in range(0,N,s):
        for j in range(0,N,s):
            if visit[i][j]==False and solve(s,i,j):
                if grid[i][j]==-1:
                    ans[0]+=1
                elif grid[i][j]==0:
                    ans[1]+=1
                elif grid[i][j]==1:
                    ans[2]+=1

    s=int(s/3)
for i in ans:
    print(i)
#print(ans)