import sys;input=sys.stdin.readline
from collections import deque
import heapq
import math
N,K=map(int,input().split())
coins=[0]*N
for i in range(N):
    coins[i]=int(input())

def solve(value,count):
    h=[]
    heapq.heappush(h,(count,value))
    while h:
        c,v=heapq.heappop(h)
        print(c,v,'adsf')
        if v==-K:
            print(c,'asdf')
            sys.exit()
        for i in range(N-1,-1,-1):
            if v-coins[i]>=-K:
                heapq.heappush(h,(c+1,v-coins[i]))

ans=0
if N==1:
    print(K)
else:
    i=-1
    temp=0
    while True:
        if temp==K:
            break
        if temp+coins[i]<=K:
            ans+=(K-temp)//coins[i]
            temp+=(K-temp)//coins[i]*coins[i]
        else:
            i-=1
    print(ans)