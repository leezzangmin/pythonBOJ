N=int(input())
temp=1
for i in range(N,0,-1):
    temp*=i
temp=str(temp)
ans=0
for i in range(-1,-len(temp),-1):
    if temp[i]=='0':
        ans+=1
    else:
        break
print(ans)
