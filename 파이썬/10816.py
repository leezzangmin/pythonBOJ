import sys;input=sys.stdin.readline
import bisect

N=int(input())
s1=sorted(list(map(int,input().split())))
M=int(input())
s2=list(map(int,input().split()))
ans=0


for i in range(M):
    print(bisect.bisect_right(s1,s2[i])-bisect.bisect_left(s1,s2[i]),end=' ')
    



# sys.stdout.write()