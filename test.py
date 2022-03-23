from itertools import combinations
op=["+","-","*",]
op=[2,1,1,1]
ops=""
for i in range(4):
    if i==0:
        for i in range(op[i]):
            ops+="+"
    elif i==1:
        for i in range(op[i]):
            ops+="-"
    elif i==2:
        for i in range(op[i]):
            ops+="*"
    else:
        for i in range(op[i]):
            ops+="/"
print(ops)
c=combinations(ops,5)
ans=0
for i in c:
    #print(i)
    ans+=1
print(ans)