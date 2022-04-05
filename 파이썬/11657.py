import sys;input=sys.stdin.readline
import heapq

def da(start):
    h=[]
    heapq.heappush(h,[start,0])
    while h:
        dest,cost = heapq.heappop(h)
        if dp[dest]<cost:
            continue
        if dp[dest]<0:
            dp[dest]=-1
        for dest_dest,cost_cost in bus[dest]:
            if dp[dest_dest]>cost+cost_cost:
                if cost+cost_cost<0:
                    dp[dest_dest]=-1
                    continue
                dp[dest_dest]=cost+cost_cost
                heapq.heappush(h,[dest_dest,cost+cost_cost])
    

N,M=map(int,input().split())

bus=[[] for _ in range(N+1)]
dp=[sys.maxsize for _ in range(N+1)]
dp[1]=0
for _ in range(M):
    A,B,C=map(int,input().split())
    bus[A].append([B,C])

da(1)
if dp.count(-1):
    print(-1)
    sys.exit()
for i in range(2,N+1):
    if dp[i]==sys.maxsize:
        print(-1)
    else:
        print(dp[i])
