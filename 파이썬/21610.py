import sys;import copy;input=sys.stdin.readline

N,M=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
move_command=[list(map(int,input().split())) for _ in range(M)]
move_direction_X=[0,   0, -1,-1,-1,0,1,1, 1]
move_direction_Y=[0,   -1,-1, 0,1, 1,1,0,-1]
cloud_list=[[N-1,0],[N-1,1],[N-2,0],[N-2,1]]


dx=[-1,1,-1,1]
dy=[-1,-1,1,1]
def four(x,y):
    for abc in range(4):
        mx=x+dx[abc]
        my=y+dy[abc]
        if 0<=mx<N and 0<=my<N and grid[mx][my]!=0:
            grid[x][y]+=1



for di,si in move_command:
    visit=[[False]*N for _ in range(N)]
    #1번
    for i in range(len(cloud_list)):
        cloud_list[i][0]=(cloud_list[i][0]+move_direction_X[di]*si)%N
        cloud_list[i][1]=(cloud_list[i][1]+move_direction_Y[di]*si)%N
    #2번
    for i in range(len(cloud_list)):
        grid[cloud_list[i][0]][cloud_list[i][1]]+=1
        visit[cloud_list[i][0]][cloud_list[i][1]]=True
    #4번
    for i in range(len(cloud_list)):
        four(cloud_list[i][0],cloud_list[i][1])

    #5번
    temp_list=list()
    for i in range(N):
        for j in range(N):
            if grid[i][j]>=2 and visit[i][j]==False:
                grid[i][j]-=2
                temp_list.append([i,j])
    #3번?                
    cloud_list=copy.deepcopy(temp_list)

ans=0
for i in grid:
    ans+=sum(i)
print(ans)