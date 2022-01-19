import sys;input=sys.stdin.readline
N=int(input())
s=[0]*N
dp=[x for x in range(1,N+1)]
for i in range(N):
    s[i]=int(input())


print(s)
print(dp)