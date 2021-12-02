import sys;input=sys.stdin.readline
N=int(input())
A=sorted(list(map(int,input().split())))
M=int(input())
B=list(map(int,input().split()))
count=0
for i in range(M):
    B[i]=(B[i],count)
    count+=1
B.sort(key=lambda x:x[0])


j=0
for i in range(M):
    while True:
        if j>=N:
            B[i]=(B[i][1],0)
            break
        if B[i][0]>A[j]:
            j+=1
        elif B[i][0]==A[j]:
            B[i]=(B[i][1],1)
            break
        elif B[i][0]<A[j]:
            B[i]=(B[i][1],0)
            break
B.sort(key=lambda x:x[0])
for i in B:
    print(i[1])