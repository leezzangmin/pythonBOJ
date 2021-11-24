import sys;input=sys.stdin.readline
from itertools import combinations
#    0 1 2 3 4 5 6 7 8 9
num=[6,2,5,5,4,5,6,3,7,6]
dp=[ [sys.maxsize,0] for _ in range(101)]
dp[2]=[1,1]
dp[3]=[7,7]
dp[4]=[4,11]
dp[5]=[2,71]
dp[6]=[6,111]
dp[7]=[8,711]
dp[8]=[10,1111]
match_min = [0, 0, 1, 7, 4, 2, 0, 8]

for i in range(9,101):
    for j in range(2,8):
        temp=str(dp[i-j][0])+str(match_min[j])
        dp[i][0]=min(dp[i][0],int(temp))

    temp1,temp2='',''
    count=i
    if i%2==0:
        for j in range(0,i,2):
            temp2+=str(1)
    else:
        temp2+=str(7)
        for j in range(0,i-3,2):
            temp2+=str(1)
    dp[i][1]=temp2


# count=0
# for i in dp:
#     print(count,end='  ')
#     print(i)
#     count+=1

T=int(input())
for _ in range(T):
    N=int(input())
    print(dp[N][0],dp[N][1])
    