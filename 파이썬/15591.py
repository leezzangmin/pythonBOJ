import sys;input=sys.stdin.readline
from collections import deque
N,Q=map(int,input().split())
graph=[[] for _ in range(N+1)]

visit=[False]*(N+1)

def dfs(usado,x,size):
    global QQ
    for mx,value in graph[x]:
        if visit[mx]==False:
            visit[mx]=True
            size=min(size,value)
            size=min(size,dfs(usado,mx,size))
            QQ.append((x,mx))
    return size
            
    

for _ in range(N-1):
    a,b,u=map(int,input().split())
    graph[a].append([b,u])
    graph[b].append([a,u])

for _ in range(Q):
    QQ=deque()
    k,video=map(int,input().split())
    visit[video]=True
    size=dfs(k,video,sys.maxsize)
    while QQ:
        x_,y_=QQ.popleft()
        graph[x_]





