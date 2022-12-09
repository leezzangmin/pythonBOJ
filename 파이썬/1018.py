import sys;input=sys.stdin.readline
N,M=map(int,input().split())
grid=list(list(input().rstrip()) for _ in range(N))
for i in grid:
    print(i)

ans=sys.maxsize

for i in range(N):
    for j in range(M):
        if i+8<N:


