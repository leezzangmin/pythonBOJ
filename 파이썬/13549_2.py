from collections import deque
import heapq
N,K=map(int,input().split())
temp=int(1e9)
maxlength=150000
street=[temp] * maxlength
street[N]=0
def bfs(first,c):
    h=[]
    # Q=deque()
    # Q.append((first,c))
    heapq.heappush(h,(c,first))
    while h:
        cost,x=heapq.heappop(h)
        if street[x]<cost:
            continue


        mx=x-1
        cc=cost+1
        if 0<=mx<maxlength and street[mx]>cc:
            street[mx]=cc
            heapq.heappush(h,(cc,mx))

        mx=x+1
        cc=cost+1
        if 0<=mx<maxlength and street[mx]>cc:
            street[mx]=cc
            heapq.heappush(h,(cc,mx))

        mx=x*2
        cc=cost
        if 0<=mx<maxlength and street[mx]>cc:
            street[mx]=cc
            heapq.heappush(h,(cc,mx))


if K<=N:
    print(abs(K-N))
else:
    bfs(N,0)
    #print(street[0:20])
    print(street[K])#,'asdf')