import sys;input=sys.stdin.readline
N,L=map(int,input().split())
grid=list(list(map(int,input().split())) for _ in range(N))
descent=list([False]*N for _ in range(N))

for i in range(N):
    if len(set(grid[i]))==1:
        descent[i]=[True]*N
    temp=[0]*N
    for j in range(N):
       temp[j]=grid[j][i]
    if len(set(temp))==1:
        for j in range(N):
            descent[j][i]=True
for i in descent:
    print(i,'d')

for i in range(N):
    for j in range(N):
        if descent[i][j]==False:

    





# 1 2 1 1 - x
# 1 2 2 2 
# 2 1 2 2 
# 1 2 1 1 - x








