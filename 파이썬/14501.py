import sys;input=sys.stdin.readline
from collections import deque
N=int(input())
t=[0]*N
p=[0]*N
dp=[0]*N
for i in range(N):
    a,b=map(int,input().split())
    t[i]=a
    p[i]=b

for i in range(N):
    Q=deque()
    Q.append(i)
