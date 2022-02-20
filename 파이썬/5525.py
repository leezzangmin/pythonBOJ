import sys;input=sys.stdin.readline
N=int(input())
M=int(input())
s=input().rstrip()
sa=[0]*M
t="IOI"
i=0
while i!=M-2:
    if s[i:i+3]==t:
        sa[i+2]=sa[i]+1
        i+=2
    else:
        i+=1
ans=0
for i in sa:
    if i>=N:
        ans+=1
print(ans)