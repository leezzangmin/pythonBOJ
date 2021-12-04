N,K=map(int,input().split())
A=sorted(list(map(int,input().split())))
psum=[0]
sum=0
for i in A:
    sum+=i
    psum.append(sum)
ans=0
for i in psum:
    if i==K:
        ans+=1