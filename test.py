import sys;input=sys.stdin.readline
import math
T=int(input())
num=3+math.sqrt(5)
dp=[0]*101
dp[0]=1
dp[1]=num
for i in range(1,101):
    dp[i]=dp[i-1]*num

print(dp[2])
for i in range(T):
    N=int(input())
    print("Case #",end='')
    print(i+1,end='')
    print(":",end=' ')
    
    if dp[N]<1000:
        print("leading zero")
    else:
        print(int(dp[N])%1000)
        #print("int(dp[N])%1000)