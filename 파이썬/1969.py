N,M=map(int,input().split())
dnas=[input() for _ in range(N)]

d='ACGT'
ans=''
h=0
for i in range(M):
    n=[0,0,0,0]
    for j in range(N):
        if dnas[j][i]=='A':
            n[0]+=1
        elif dnas[j][i]=='C':
            n[1]+=1
        elif dnas[j][i]=='G':
            n[2]+=1
        elif dnas[j][i]=='T':
            n[3]+=1
    temp=0
    index=123
    for i in range(-1,-len(n)-1,-1):
        if n[i]>=temp:
            temp=n[i]
            index=i
    for i in range(-1,-len(n)-1,-1):
        if i!=index:
            h+=n[i]
    ans+=d[index]
print(ans)
print(h)
