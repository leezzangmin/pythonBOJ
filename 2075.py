
ans=0
for i in range(1,872315):
    b=str(i)
    ans+=b.count('1')
    if i%15000==0:
        print(b)
print(ans)