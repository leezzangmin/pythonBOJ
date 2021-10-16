X=int(input())
a=bin(X)

ans=0
for i in range(2,len(a)):
    if a[i]=='1':
        ans+=1
print(ans)


# print(bin(int(input())).count('1'))