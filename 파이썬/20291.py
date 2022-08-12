import sys;input=sys.stdin.readline
N=int(input())
ans=dict()
for _ in range(N):
    _,s=input().rstrip().split('.')
    if s in ans.keys():
        ans[s]+=1
    else:
        ans[s]=1
aaa=sorted(ans.items())
for i in aaa:
    print(i[0],i[1])

