import copy
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
B2=sorted(B)
B2.reverse()
INDEX=[]
B3=copy.deepcopy(B2)
for i in B:
    INDEX.append(B2.index(i))
    B2[INDEX[-1]]=-123
A.sort()
ans=0
for i in range(N):
    ans+=B3[INDEX[i]]*A[INDEX[i]]
print(ans)

# 이게 코드냐 ㅋㅋㅋㅋㅋㅋㅋㅋ
