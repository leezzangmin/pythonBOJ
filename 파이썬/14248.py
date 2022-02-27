import sys;input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**8)

N=int(input())
d=list(map(int,input().split()))
visit=[False]*N
s=int(input()) - 1


def bfs():
    count=0
    Q=deque()
    Q.append(s)
    while Q:
        location=Q.popleft()
        visit[location]=True
        for i in (location+d[location],location-d[location]):
            if 0<=i<N and visit[i]==False:
                Q.append(i)
                count+=1
    return count

def dfs(s):
    visit[s]=True
    for i in (s+d[s],s-d[s]):
        if 0<=i<N and visit[i]==False:
            dfs(i)


dfs(s)
ans=visit.count(True)
print(ans)