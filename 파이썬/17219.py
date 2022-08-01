import sys;input=sys.stdin.readline
N,M=map(int,input().split())
d=dict()
for _ in range(N):
    c=input().split()
    d[c[0]]=c[1]
for _ in range(M):
    a=input().rstrip()
    print(d[a])