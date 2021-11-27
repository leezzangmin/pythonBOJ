import sys
input=sys.stdin.readline
X,Y=map(int, input().rsplit())

Z = Y * 100 // X
# (y + mid) * 100 // (x + mid)
ans = sys.maxsize
left,right=1,X

while left<=right:
    mid=(left+right)//2
    temp=(Y+mid)*100//(X+mid)

    if Z>=temp:
        left=mid+1
    else:
        ans=mid
        right=mid-1
if ans==sys.maxsize:
    print(-1)
else:
    print(ans)

    