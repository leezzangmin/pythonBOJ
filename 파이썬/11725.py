import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**8)

N=int(input())
graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visit=[False]*(N+1)
result=[0]*(N+1)
def dfs(x):
    visit[x]=True
    for mx in graph[x]:
        if visit[mx]==False:
            result[mx]=x
            dfs(mx)

    


dfs(1)
for i in range(2,N+1):
    print(result[i])
#print(result)
#        1
#      6  4
#    3   2 7
#   5