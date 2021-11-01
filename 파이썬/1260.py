import sys;
input=sys.stdin.readline;
from collections import deque
sys.setrecursionlimit(10000000)

def dfs(start):
    visit[start]=True
    ans1.append(start)
    for i in graph[start]:
        if visit[i]==False:
            dfs(i)

def bfs(start):
    visit[start]=True
    q=deque([start])
    while q:
        temp=q.popleft()
        ans2.append(temp)
        for i in graph[temp]:
            if visit[i]==False:
                q.append(i)
                visit[i]=True

if __name__=="__main__":
    ans1,ans2=[],[]
    N,M,V=map(int,input().split())
    graph=[ [] for _ in range(N+1) ]
    for i in range(M):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,N+1):
        graph[i].sort()


    
    visit=[False]*(N+1)
    dfs(V)


    visit=[False]*(N+1)
    bfs(V)

    for i in ans1:
        print(i,end=' ')
    print()
    for i in ans2:
        print(i,end=' ')
    print()

