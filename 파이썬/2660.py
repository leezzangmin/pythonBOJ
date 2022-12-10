import sys;input=sys.stdin.readline
from collections import deque
N=int(input())

graph=[ [] for _ in range(N+1)]
score=[ 0 for _ in range(N+1)]
while True:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    graph[a].append(b)
    graph[b].append(a)


#print(graph)

for i in range(1,N+1):
    for x in graph[i]:
        score[i]+=1
#print(score,'asdf')
m=max(score)


print(N-m,score.count(m))
for i in range(1,N+1):
    if score[i]==m:
        print(i,end=' ')