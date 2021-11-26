N=int(input())
s=list(map(int,input().split()))
s.sort()
ans=0
for i in range(N):
    ans+=sum(s[0:i+1])
print(ans)
