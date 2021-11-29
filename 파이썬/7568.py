N=int(input())
s=[]
for _ in range(N):
    s.append( list(map(int,input().split())) )
#print(s)
temp=[1]*N
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if s[i][0]<s[j][0] and s[i][1]<s[j][1]:
            temp[i]+=1
print(*temp)
