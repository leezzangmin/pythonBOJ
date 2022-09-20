import sys;input=sys.stdin.readline
N=int(input())

graph=[[] for _ in range(N)]
for i in range(N):
    temp=list(map(int,input().split()))
    for j in range(N):
        if temp[j]==1:
            graph[i].append(j)
grid=[[False]*N for _ in range(N)]
for i in range(N):
    grid[i][i]=True
for i in grid:
    print(i)



