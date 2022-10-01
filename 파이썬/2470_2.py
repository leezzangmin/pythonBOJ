import sys;input=sys.stdin.readline
N=int(input())
yong=sorted(list(map(int,input().split())))


# 0에 가장 가까운 용액 만들기
l,r=0,N-1
minval=sys.maxsize
left_y,right_y=l,r
while l<r:
    temp=yong[l]+yong[r]
    if temp==0:
        print(yong[l],yong[r])
        exit()

    if minval>abs(temp):
        minval=abs(temp)
        left_y,right_y=yong[l],yong[r]
    
    if temp<0:
        l+=1
    elif temp>0:
        r-=1
print(left_y,right_y)

# -5 -4 -3 -2 -1 0 1 2 3 4 5

# 0 