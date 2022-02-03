import sys;input=sys.stdin.readline;sys.setrecursionlimit(10**8)
N=int(input())
grid=[0]*N
visit=[False]*N
ansL=[]
for i in range(N):
    temp=int(input())
    if i+1==temp:
        ansL.append(temp)
        visit[i]=True
    grid[i]=temp

def dfs(target, cnt,init):
    tempL.add(grid[target])
    visit[target]=True
    M_target=grid[target]-1
    if visit[ M_target ] == False:
        dfs(M_target,cnt+1,init)
    else:
        if grid[M_target] == grid[init]:
            tempL.add(grid[M_target])
            return
        

tempL2=[]
for i in grid:
    visit=[False]*N
    tempL=set()
    dfs(i-1,1,i)
    if len(tempL)>len(tempL2):
        tempL2=tempL
      

for i in tempL2:
    ansL.append(i)

print(len(ansL))
ansL.sort()
for i in ansL:
    print(i)


