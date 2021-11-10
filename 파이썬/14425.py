import sys;input=sys.stdin.readline
N,M=map(int,input().split())
s1=list(input() for _ in range(N))
s2=list(input() for _ in range(M))

ans=0
for i in range(M):
    if s2[i] in s1:
        ans+=1
print(ans)