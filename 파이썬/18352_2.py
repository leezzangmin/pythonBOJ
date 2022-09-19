import sys;input=sys.stdin.readline
from collections import deque

N,M,K,X=map(int,input().split())
graph=[[] for _ in range(N+1)]


for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
distances=[sys.maxsize]*(N+1)
visit = [False]*(N+1)
distances[X]=0

Q=deque()
Q.append((X,0))
while Q:
    x,dist=Q.popleft()
    for i in graph[x]:
        if distances[i]==sys.maxsize:
            distances[i]=dist+1
            Q.append((i,dist+1))



flag=False
for i in range(1,len(distances)):
    if distances[i]==K:
        print(i)
        flag=True
if flag==False:
    print(-1)

