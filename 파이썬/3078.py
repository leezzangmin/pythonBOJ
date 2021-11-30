import sys;input=sys.stdin.readline
N,K=map(int,input().split())

student=list(len(input()) for _ in range(N))

ans=0
for i in range(0,N-1):
    for j in range(i+1,i+K+1):
        print(i,j)
        if student[i]==student[j]:
                ans+=1
print(ans)