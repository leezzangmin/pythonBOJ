import sys;input=sys.stdin.readline;import heapq

N=int(input())

s=[]
for i in range(N):
    a=int(input())
    if a!=0:
        heapq.heappush(s,-a)
    else:
        if s:
            print(-heapq.heappop(s))
        else:
            print(0)