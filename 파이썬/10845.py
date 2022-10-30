import sys;input=sys.stdin.readline
from collections import deque
N=int(input())
temp=deque()
size=0
for _ in range(N):
    command=input().rstrip().split()
    if command[0]=='push':
        temp.append(command[1])
        size+=1
    elif command[0]=='pop':
        if size==0:
            print(-1)
        else:
            a=temp.popleft()
            print(a)
            size-=1
    elif command[0]=='size':
        print(size)
    elif command[0]=='empty':
        if size==0:
            print(1)
        else:
            print(0)
    elif command[0]=='front':
        if size==0:
            print(-1)
        else:
            print(temp[0])
    elif command[0]=='back':
        if size==0:
            print(-1)
        else:
            print(temp[-1])


