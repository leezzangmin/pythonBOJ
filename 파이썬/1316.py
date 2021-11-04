import sys;input=sys.stdin.readline
N=int(input())
ans=0
for _ in range(N):
    s=input().rstrip()
    temp=[]
    f=True
    for i in range(len(s)):
        if s[i] in temp:
            if temp[-1]==s[i]:
                pass
            else:
                f=False
                break
        else:
            temp.append(s[i])

    if f:
        ans+=1
print(ans)