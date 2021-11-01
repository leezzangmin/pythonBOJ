import sys;input=sys.stdin.readline
A,B=map(int,input().split())
Alist=list(map(int,input().split()))
Blist=list(map(int,input().split()))

temp=set(Alist+Blist)
s=len(temp)


ans=s-A + s-B
print(ans)