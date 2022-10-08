import sys;input=sys.stdin.readline
from collections import deque
N,M=map(int,input().split())

graph=[[] for _ in range(N+1)]
for i in range(M):
    A,B,C=map(int,input().split())
    graph[A].append([C,B])
    graph[B].append([C,A])
for i in graph:
    i.sort(key=lambda x:-x[0])
start,dest=map(int,input().split())

l,r=1,sys.maxsize
answer=0
while l<=r:
    mid=(l+r)//2
    flag=False
    
    visit=[False]*(N+1)
   
    Q=deque()
    Q.append(start)
    while Q:
        x=Q.popleft()
        if x==dest:
            flag=True
            break
        for cost,mx in graph[x]:
            if visit[mx]==False and cost>=mid:
                visit[mx]=True
                Q.append(mx)
    if flag:
        answer=mid
        l=mid+1
    else:
        r=mid-1

print(answer)

# 10000 3
# 9998 9999 2
# 10000 9998 3
# 9999 10000 2
# 9998 10000
    
    