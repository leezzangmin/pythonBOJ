import sys;input=sys.stdin.readline
import heapq

N,D=map(int,input().split())
graph = [[] for _ in range(D+1)]
for i in range(D):
    graph[i].append((i+1, 1))
distance=[987654321]*10001
distance[0]=0
for _ in range(N):
    start,dest,length=map(int,input().split())
    if dest>D:
        continue
    graph[start].append((dest,length))

# h=[]
# heapq.heappush(h,(0,0))
# while h:
#     dist,now=heapq.heappop(h)
#     if distances[now]<dist:
#         continue
#     for dest,length in graph[now]:
#         cost=dist+length
#         print(distances,dest)
#         if cost < distances[dest]:
#             distances[dest]=cost
#             heapq.heappush(h,(cost,dest))



q = []
heapq.heappush(q, (0, 0))
while q:
    d, now = heapq.heappop(q)
    if distance[now] < d: continue

    for x in graph[now]:
        cost = d + x[1]

        if distance[x[0]] > cost:
            distance[x[0]] = cost
            heapq.heappush(q, (cost, x[0]))

print(distance[D])