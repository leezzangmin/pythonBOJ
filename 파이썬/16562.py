ohno='Oh no'
import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import deque
N,M,money=map(int,input().split())
graph=[[x] for x in range(N)]
A=list(map(int,input().split()))
for _ in range(M):
    a,b=map(int,input().split())
    if a!=b:
        if b-1 not in graph[a-1]:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)


def dfs(x,cost):
    visit[x]=True
    for mx in graph[x]:
        if visit[mx]==False:
            cost=min(cost,dfs(mx,A[mx]))
    return cost
visit=[False]*N

spent=0
for i in range(N):    
    if visit[i]==False:
        spent+=dfs(i,A[i])
       # print(spent,'spent',i)
if spent>money:
    print(ohno)
else:
    print(spent)
#print(visit.count(False),'count')
#print(to_spent)
