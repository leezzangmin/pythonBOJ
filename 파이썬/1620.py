import sys;input=sys.stdin.readline

N,M=map(int,input().split())

poketmon={}

for i in range(1,N+1):
    poketmon[input().rstrip()]=i

Lpoketmon=list(poketmon.keys())

for i in range(M):
    s=input().rstrip()
    if s.isdigit():
        print(Lpoketmon[int(s)-1])
    else:
        print(poketmon[s])