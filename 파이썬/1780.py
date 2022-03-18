import sys;
input=sys.stdin.readline
N=int(input())
grid=list( list(map(int,input().split())) for _ in range(N) )

ans=[0,0,0] # -1, 0, 1
for i in grid:
    print(i)


def sol(x,y,size):
    target=grid[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if grid[i][j]!=target:
                return
                
    if target==-1:
        ans[0]+=1
    elif target==0:
        ans[1]+=1
    else:
        ans[2]+=1
    return


sol(0,0,N)



print(ans)