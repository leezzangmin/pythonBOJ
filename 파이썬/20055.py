import sys;input=sys.stdin.readline
from collections import deque
N,K=map(int,input().split())
A=list(map(int,input().split()))
robot=[0]*(N*2)
naegoo=0

left=0
right=N-1

second=0
while naegoo<K:

    left -= 1
    if left==-1:
        left=(2*N)-1
    right -=1
    if right==-1:
        right=(2*N)-1
    robot[right]=0
    
    for i in range(left+N-1,left-1,-1):
        j=(i+1) % (2*N)
        i=i%(2*N)
        #print(i,j,'ijij')

        if robot[i]==1:
            if robot[j]==1:
                continue
            if A[j]!=0:
                robot[i]=0
                robot[j]=1
                A[j]-=1
                if A[j]==0:
                    naegoo+=1

    if A[left]!=0:
        A[left]-=1
        if A[left]==0:
            naegoo+=1
        robot[left] = 1
    robot[right]=0


    second+=1

print(second)