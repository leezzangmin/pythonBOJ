import sys;input=sys.stdin.readline
N=int(input())

start=dict()
for i in range(N):
    start[input().rstrip()]=i
end=dict()
for i in range(N):
    end[input().rstrip()]=i

ans=0
for ks,vs in end.items():
    for ke,ve in start.items():
        if start[ke]<start[ks] and end[ks]<end[ke]:
            ans+=1
            break
print(ans)