import math
N=int(input())
sosu=[True for x in range(N+1)]
for i in range(2,int(math.sqrt(N))+1):
    if sosu[i]:
        j=2
        ij=i*j
        while ij<=N:
            sosu[ij]=False
            j+=1
            ij=i*j
_sosu=[i for i in range(2,N+1) if sosu[i]]+[0]

start,end=0,0
ans=0
s=_sosu[start]
while end<len(_sosu)-1:
    if s==N:
        ans+=1
        s-=_sosu[start]
        start+=1

    elif s<N:
        end+=1
        s+=_sosu[end]
    elif s>N:
        s-=_sosu[start]
        start+=1
        
print(ans)
