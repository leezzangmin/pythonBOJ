from itertools import product
T=int(input())
dp=[0]*10000
a=[1,2,3]
for i in range(1,12):
    p=product(a,repeat=i)
    for j in p:
        dp[sum(j)]+=1



for _ in range(T):
    print(dp[int(input())])
