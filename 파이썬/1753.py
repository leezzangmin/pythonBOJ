import sys;input=sys.stdin.readline
import heapq

V,E=map(int,input().split())
K=int(input())

graph=[[] for _ in range(V+1)]
INF=987654321
distance=[INF]*(V+1)
distance[K]=0

for _ in range(E):
    start,end,weight=map(int,input().split())
    graph[start].append((end,weight))

h=[]
heapq.heappush(h,(0,K))
while h:
    dist,now=heapq.heappop(h)
    if distance[now]<dist:
        continue
    for destination, weight in graph[now]:
        cost=dist+weight
        if distance[destination]>cost:
            distance[destination]=cost
            heapq.heappush(h,(cost,destination))
for i in range(1,V+1):
    if distance[i]!=INF:
        print(distance[i])
    else:
        print('INF')