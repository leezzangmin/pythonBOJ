import sys;input=sys.stdin.readline

N=int(input())

left = 1
right = 2

ans=0
if N==1:
    print(1)
    sys.exit()

temp=right+left
while left<=N:
    if temp<N:
        right+=1
        temp+=right
    elif temp==N:
        ans+=1
      #  print(left,right,'asdf')
        temp-=left
        left+=1
        right+=1
        temp+=right
    elif temp>N:
        temp-=left
        left+=1
print(ans)