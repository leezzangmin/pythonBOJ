import sys;input=sys.stdin.readline
from collections import deque
N,M=map(int,input().split())
parking=[0]*(N+1)
price=[int(input()) for _ in range(N)]
weight=[int(input()) for _ in range(M)]
action=deque(int(input()) for _ in range(2*M))

ans=0
wating=deque()
for i in range(len(action)):
    car=action.popleft()

    if car>0:
        if 0 in parking[1:]:
            for j in range(1,N+1):
                if parking[j]==0:
                    parking[j]=car
                    ans+=price[j-1]*weight[parking[j]-1]
                    break
        else:
            wating.append(car)

            
    else:
        for i in range(1,(N+1)):
            if parking[i]==-car:
                parking[i]=0
                break
        if wating:
            car=wating.popleft()
            for j in range(1,N+1):
                if parking[j]==0:
                    parking[j]=car
                    ans+=price[j-1]*weight[parking[j]-1]
                    break

print(ans)