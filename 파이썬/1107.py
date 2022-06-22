import sys;input=sys.stdin.readline
target=int(input())
broken_number=int(input())
broken_button=list()
if broken_number!=0:
    broken_button=list(map(str,input().split()))

ans = abs(target-100)

for s in range(1000001):
    ss=str(s)
    flag=True
    for j in ss:
        if j in broken_button:
            flag=False
            break
    if flag:
        ans=min(ans,abs(target-s)+len(ss))

print(ans)


