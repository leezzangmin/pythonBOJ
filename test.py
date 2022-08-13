import sys
a=sys.maxsize*100
ans=0
for i in range(40000):
    for j in range(i+1,40000):
        ans+=1
print(ans)