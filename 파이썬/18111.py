import sys;input=sys.stdin.readline;import math
N,M,B=map(int,input().split())
grid=[ list(map(int,input().split())) for _ in range(N) ]
MIN=sys.maxsize
MAX=-1
for i in range(N):
    for j in range(M):
        t=grid[i][j]
        MIN=min(MIN,t)
        MAX=max(MAX,t)


ans=[sys.maxsize,sys.maxsize]
for h in range(MIN,MAX+1):
    time=0
    blocks=B
    for i in range(N):
        for j in range(M):
            t=grid[i][j]
            if t>h:
                blocks+=t-h
                time+=2*(t-h)
            elif t<h:
                blocks=blocks-(h-t)
                time+=h-t
            

    if blocks<0:
        continue
    if time<=ans[0]:
        if time==ans[0]:
            ans[1]=max(h,ans[1])
        else:
            ans=[time,h]
print(ans[0],ans[1])
