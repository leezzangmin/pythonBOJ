import sys;input=sys.stdin.readline
import heapq

N,D=map(int,input().split())
dist=[i for i in range(D+1)]

Q=[]
for _ in range(N):
    start,destination,length=map(int,input().split())

    if destination>D:
        continue
    heapq.heappush(Q,(start,destination,length))


while Q:
    start,dest,len = heapq.heappop(Q)
    if dist[dest]<dist[start]+len:
        continue
    else:
        dist[dest]=dist[start]+len
        for i in range(dest+1,D+1):
            dist[i]=min(dist[i],dist[i-1]+1)
print(dist[-1])