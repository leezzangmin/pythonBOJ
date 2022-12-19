grid=list(input() for _ in range(5))
m=0
for i in grid:
    m=max(m,len(i))

ans=''
for j in range(m):
    temp=''
    for i in range(16):
        try:
            grid[i][j]
        except:
            continue
        temp+=grid[i][j]
    ans+=temp
print(ans)