import sys;input=sys.stdin.readline
N,K=map(int,input().split())
coins=[0]*N
dp=[sys.maxsize]*(K+1)
dp[0]=1
for i in range(N):
    coins[i]=int(input())
    try:
        dp[coins[i]]=1
    except:
        pass
    
for i in range(N):
    c=coins[i]
    for j in range(c,K+1):
        dp[j]=min(dp[j-c]+1,dp[j])



#print(dp)
if dp[K]==sys.maxsize:
    print(-1)
else:
    print(dp[K])
