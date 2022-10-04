from collections import defaultdict
lw,ls=map(int,input().split())

W=input()
S=input()

ans=0

ww=[0]*58
for i in range(lw):
    index=ord(W[i])-65
    ww[index]+=1
ss=[0]*58
ssl=0
for i in range(ls):
    ss[ord(S[i])-65]+=1
 #   print(ss)
    ssl+=1

    if ssl==lw:
        if ww==ss:
            ans+=1
        ss[ord(S[i-lw+1])-65]-=1
        ssl-=1
    

print(ans)