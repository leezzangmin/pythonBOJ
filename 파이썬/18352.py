import sys;input=sys.stdin.readline
from collections import deque
num_of_city,num_of_road,road_info,start_city_num=map(int,input().split())
graph=[[] for _ in range(num_of_city+1)]
for _ in range(num_of_road):
    A,B=map(int,input().split())
    graph[A].append(B)


Q=deque()
Q.append((start_city_num,0))
distance=[sys.maxsize]*(num_of_city+1)
visit=[False]*(num_of_city+1)
distance[start_city_num]=0

while Q:
    x,dist=Q.popleft()
    visit[x]=True
    if dist>distance[x]:
        continue
    if dist==road_info:
        continue
    for i in graph[x]:
        if visit[i]==False:
            Q.append((i,dist+1))
            if distance[i]>dist+1:
                distance[i]=dist+1
count=0
for i in range(len(distance)):
    if distance[i]==road_info:
        print(i)
        count+=1
if count==0:
    print(-1)

