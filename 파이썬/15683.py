import sys;input=sys.stdin.readline
from collections import deque;import copy
N,M=map(int,input().split())
grid=list(list(map(int,input().split())) for _ in range(N))

def dfs(depth,grid):
    global answer
    # 종료 조건: 모든 CCTV 탐색
    if depth == len(cctvs):
        # 사각지대 최솟값
        answer = min(answer, count_zero(grid))
        return
    temp_grid=copy.deepcopy(grid)
    x,y,level=cctvs[depth]
    for i in cctv_watch[level]:
        asdf(x,y,i,temp_grid)
        dfs(depth+1,temp_grid)
        temp_grid=copy.deepcopy(grid)
            

def asdf(x,y,direction,graph):
    for d in direction:
        nx, ny = x, y
        # 특정 방향으로 벽을 만나거나 사무실을 벗어나기 전까지 탐색
        while True:
            nx += dx[d]
            ny += dy[d]
            # 맵 내 위치
            if 0 <= nx < N and 0 <= ny < M:
                # 벽을 만난 경우
                if graph[nx][ny] == 6:
                    break
                # 새로운 감시가능 영역일 경우
                elif graph[nx][ny] == 0:
                    graph[nx][ny] = '#'
            # 맵 외 위치
            else:
                break
def count_zero(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

# 좌 하 우 상
dx=[0,1,0,-1] 
dy=[-1,0,1,0]
cctv_watch=[
    [[0],[1],[2],[3]], 
    [[0,2],[1,3]],
    [[2,3],[0,3],[0,1],[1,2]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]]
answer=111111111
cctvs=[]
for i in range(N):
    for j in range(M):
        t=grid[i][j]
        if t!=0 and t!=6:
            cctvs.append([i,j,t-1])

dfs(0,grid)
print(answer)