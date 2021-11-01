import sys;input=sys.stdin.readline
N,K=map(int,input().split())

student=list(len(input()) for _ in range(N))


ans=0
for i in range(N):
    for j in range(i+1,i+K+1):
        if j<N:
            if student[i]==student[j]:
                ans+=1
        else:
            break


print(ans)