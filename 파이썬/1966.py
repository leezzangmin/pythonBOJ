import sys;input=sys.stdin.readline
from collections import deque
import heapq

T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    d=list(map(int,input().split()))
    Q=[]
    j=0
    for i in d:
        heapq.heappush(Q,(-i,j))
        j+=1
    count=1
    while Q:
        print(Q)
        _,tmp = heapq.heappop(Q)
        if tmp==M:
            print(count,'asdfasdf')
        count+=1
            

    #print(Q,'asdf')
    
        