import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**6)
import heapq
N,M=map(int,input().split())
graph=[ [] for _ in range(N+1)]
for _ in range(M):
    A,B=map(int,input().split())
    graph[B].append(A)

def dfs(x,count):
    visit[x]=True
    for xx in graph[x]:
        if visit[xx]==False:
            count=max(count,dfs(xx,count+1))
    return count
temp_max=0
ans=[]
for i in range(1,N+1):
    visit=[False]*(N+1)
#    if visit[i]==False:
    ff=dfs(i,1)
    if ff>=temp_max:
        temp_max=ff
        heapq.heappush(ans,(ff,i))
ans.sort(key=lambda x:(-x[0],x[1]))
for x,y in ans:
    if temp_max==x:
        print(y,end=' ')
    else:
        break
