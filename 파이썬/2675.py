import sys;input=sys.stdin.readline
T=int(input())
for _ in range(T):
    r,s=input().split()
    for i in s:
        for _ in range(int(r)):
            print(i,end='')
    print()