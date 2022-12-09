import sys;input=sys.stdin.readline
import heapq;import copy
N,E=map(int,input().split())
graph = [ [] for _ in range(N+1)]

answer=0
def da(start):
    dist[start]=0
    h=[]
    heapq.heappush(h,(0,start))
    while h:
        d,now=heapq.heappop(h)
        if dist[now]<d:
            continue
        for x in graph[now]:
            if x[1]:
                pass
            if d+x[1]<dist[x[0]]:
                dist[x[0]]=d+x[1]
                heapq.heappush(h,(d+x[1],x[0]))

for _ in range(E):
   a,b,c=map(int,input().split())
   graph[a].append((b,c))
   graph[b].append((a,c))

v1,v2=map(int,input().split())
dist=[sys.maxsize]*(N+1)
da(1)

dist1=copy.deepcopy(dist)


dist=[sys.maxsize]*(N+1)
da(v1)
dist2=copy.deepcopy(dist)


dist=[sys.maxsize]*(N+1)
da(v2)
dist3=copy.deepcopy(dist)

answer1=dist1[v1]+dist2[v2]+dist3[N]
answer2=dist1[v2]+dist3[v1]+dist2[N]
answer=min(answer1,answer2)
if answer>=sys.maxsize:
    print(-1)
else:
    print(answer)