import sys;input=sys.stdin.readline
from collections import defaultdict
N,d,k,c=map(int,input().split())
sushi=[int(input()) for _ in range(N)]

gaji=defaultdict(int)
i,j=0,0


gaji[c]+=1
while j < k:
    gaji[sushi[j]] += 1
    j += 1

ans=len(gaji)
while i<N:
    gaji[sushi[i]]-=1
    if gaji[sushi[i]]==0:
        del gaji[sushi[i]]
    i+=1
    j=j%N
    gaji[sushi[j]]+=1
    j+=1
    ans=max(ans,len(gaji))
print(ans)
