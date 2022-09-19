import sys;input=sys.stdin.readline
N=int(input())
numbers=[int(input()) for _ in range(N)]
pos=[]
neg=[]
for i in numbers:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)
pos.sort()
neg.sort()
# -5 -4 -3 0 1 2 3 4


ans=0
i=len(pos)-1
l=len(pos)
while i>0:
    if pos[i]!=1 and pos[i-1]!=1:
        ans+=(pos[i]*pos[i-1])
        i-=2
    else:
        ans+=(pos[i]+pos[i-1])
        i-=2
if i==0:
    ans+=pos[i]

i=0
l=len(neg)
while i<l-1:
    ans+=(neg[i]*neg[i+1])
    i+=2

if i==l-1:
    ans+=neg[i]

print(ans)
