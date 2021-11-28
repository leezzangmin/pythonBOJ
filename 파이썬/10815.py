N=int(input())
_N=list(map(int,input().split()))
_N.sort()
M=int(input())
_M=list(map(int,input().split()))

import bisect
for i in range(M):
    try:
        if _N[bisect.bisect_left(_N,_M[i])]==_M[i]:
            print(1,end=' ')
        else:
            print(0,end=' ')
    except:
        print(0,end=' ')
