import sys;input=sys.stdin.readline
import heapq

N,M=map(int,input().split())
graph1=[[] for _ in range(N+1)]
graph2=[[] for _ in range(N+1)]
for i in range(M):
    A,B=map(int,input().split())
    graph1[A].append(B)
    graph2[B].append(A)
print(graph1)
print(graph2)
def kevin_bacon(x):
    asdf=0
    Q=[]
    heapq.heappush(Q,x)
    for j in range(1,N+1):
        if j==x:
            continue
        




    return asdf 

ans=sys.maxsize
#for i in range(1,N+1):
#    ans=min(ans,kevin_bacon(i))


