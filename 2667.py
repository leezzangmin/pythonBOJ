import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**8)


def dfs(x,y):
    global temp
    temp+=1
    visit[x][y]=True
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if 0<=mx<N and 0<=my<N:
            if visit[mx][my]==False and grid[mx][my]=='1':
                dfs(mx,my)

if __name__=="__main__":
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    N=int(input())
    grid=list(input().rstrip() for _ in range(N))
    visit=[[False]*N for _ in range(N)]
    ans=[]
    for i in range(N):
        for j in range(N):
            if visit[i][j]==False and grid[i][j]=='1':
                temp=0
                dfs(i,j)
                ans.append(temp)

    print(len(ans))
    ans.sort()
    for i in ans:
        print(i)
