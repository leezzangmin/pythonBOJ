import sys;input=sys.stdin.readline
K,N=map(int,input().split())

cable=list(int(input()) for _ in range(K))

l,r=0,sys.maxsize
answer=0
while l<=r:
    mid=(l+r)//2
    print(mid,'mid')
    temp=0
    for c in cable:
        temp+=c//mid
        if temp>N:
            break
    
    if temp>=N:
        answer=mid
        l=mid+1
        
    else:
        r=mid-1
print(answer)