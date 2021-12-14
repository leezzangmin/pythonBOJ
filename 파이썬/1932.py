import sys;input=sys.stdin.readline
N=int(input())

s=list(list(map(int,input().split()))for _ in range(N))
if N==1:
    print(s[0][0])
    sys.exit()
s[1][0]+=s[0][0]
s[1][1]+=s[0][0]


for i in range(2,N):
    s[i][0]+=s[i-1][0] #처음
    s[i][-1]+=s[i-1][-1] #끝
    for j in range(1,i):
        s[i][j]+=max(s[i-1][j-1],s[i-1][j]) #중간

print( max(s[-1]))
