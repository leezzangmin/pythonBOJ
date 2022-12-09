import sys;input=sys.stdin.readline
T=int(input())
N=int(input())
A=list(map(int,input().split()))
psumA=[0]*(N+1)
temp=0
for i in range(N):
    temp+=A[i]
    psumA[i+1]=temp

M=int(input())
B=list(map(int,input().split()))
psumB=[0]*(M+1)
temp=0
for i in range(M):
    temp+=B[i]
    psumB[i+1]=temp
print(A,'A')
print(B,'B')
print(psumA,'psumA')
print(psumB,'psumB')
for i in range(1,N+1):
    temp=0
    
