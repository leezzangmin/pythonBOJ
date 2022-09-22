T=int(input())
for _ in range(T):

    s=input()
    ls=len(s)
    temp=0
    ans=0
    for i in range(len(s)):
        if s[i]=='X':
            temp=0
        else:
            temp+=1
        ans+=temp
    print(ans)