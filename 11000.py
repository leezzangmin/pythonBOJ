import sys;input=sys.stdin.readline
from queue import PriorityQueue
N=int(input())
c=list( list( map(int,input().split()) ) for _ in range(N) )
c.sort()

q=PriorityQueue()
q.put(c[0])
ans=1
for i in range(1,N):
    temp=q.get()
    
    if temp[1]>=c[i][0]:
        q.put(c[i])
    else:
        q.put(temp)
        q.put(c[i])


    ans=max(ans,q.qsize())
print(ans)