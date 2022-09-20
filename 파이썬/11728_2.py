import sys;input=sys.stdin.readline
A,B=map(int,input().split())
A_list=list(map(int,input().split()))
B_list=list(map(int,input().split()))

res=[]
i,j=0,0
while i<A and j<B:
    if A_list[i]<B_list[j]:
        res.append(A_list[i])
        i+=1
    elif A_list[i]>B_list[j]:
        res.append(B_list[j])
        j+=1
    else:
        res.append(A_list[i])
        res.append(A_list[i])
        i+=1
        j+=1

if i==A:
    for k in range(j,B):
        res.append(B_list[k])
else:
    for k in range(i,A):
        res.append(A_list[k])

print(*res)
#for i in res:
#    print(i,end=' ')