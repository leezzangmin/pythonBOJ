from bisect import bisect_left
N=int(input())
X=list(map(int,input().split()))
X2=sorted(list(set(X)))

for i in range(N):
    
    print(bisect_left(X2,X[i]),end=' ')

