N=int(input())

ans=0
for i in range(1,N+1):
    s=str(i)

    
    j=len(s)
    
    if len(s)<=2:
        ans+=1
        continue
    flag=True
    idx=0
    cha=int(s[idx])-int(s[idx+1])
    idx+=1
    while idx<j-1:
        if int(s[idx])-int(s[idx+1]) == cha:
            pass
        else:
            flag=False
        idx+=1




    if flag:
        ans+=1



print(ans)