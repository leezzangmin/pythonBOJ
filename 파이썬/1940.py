import sys;input=sys.stdin.readline
N=int(input())
M=int(input())
s=sorted(list(map(int,input().split())))
L=0;R=N-1
ans=0
while L<R:
    suit=s[L]+s[R]
    if suit<M:
        L+=1
    elif suit>M:
        R-=1
    elif suit==M:
        ans+=1
        L+=1
        R-=1
print(ans)