import sys;input=sys.stdin.readline

N,M=map(int,input().split())
R=list(map(int,input().split()))

l=max(R)
r=sum(R)
ans=sys.maxsize
while l<=r:
    mid = int((l+r)/2)
    s=0;count=1
    for i in range(N):
        if s+R[i]>mid:
            count+=1
            s=R[i]
        else:
            s+=R[i]

    if count<=M:
        ans=min(ans,mid)
        r=mid-1
    else:
        l=mid+1
print(ans)