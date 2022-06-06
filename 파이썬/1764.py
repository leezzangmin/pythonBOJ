import sys;input=sys.stdin.readline

N,M=map(int,input().split())

d={}
for _ in range(N+M):
    s=input().rstrip()
    if s in d:
        d[s]+=1
    else:
        d[s]=1
dd=[]
for i in d:
    if d[i]==2:
        dd.append(i)
dd.sort()
print(len(dd))
for i in dd:
    print(i)
