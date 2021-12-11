import sys;input=sys.stdin.readline
N,K=map(int,input().split())
s=list(map(int,(input().split())))
#print(s)

ans=-sys.maxsize
temp=sum(s[0:K])
#print(temp)
L=0
R=K
for i in range(K,N):
    ans=max(ans,temp)
    temp=temp-s[L]+s[R]
    #print(temp)
    L+=1;R+=1
print(max(ans,temp))

