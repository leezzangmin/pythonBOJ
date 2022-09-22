import sys;input=sys.stdin.readline
from itertools import combinations
N=int(input())
grid=[list(input().split()) for _ in range(N)]
empty=[]
teacher=[]
#s_count=0
for i in range(N):
    for j in range(N):
        if grid[i][j]=='X':
            empty.append((i,j))
        elif grid[i][j]=='T':
            teacher.append((i,j))
       # elif grid[i][j]=='S':
       #     s_count+=1


dx=[0,0,1,-1]
dy=[1,-1,0,0]

def search():
    for x,y in teacher:
        mx=x+1
        while 0<=mx<N:
            
            if grid[mx][y]=='S':
                return 1
            elif grid[mx][y]=='O':
                break
            mx+=1
        mx=x-1
        while 0<=mx<N:
            
            if grid[mx][y]=='S':
                return 1
            elif grid[mx][y]=='O':
                break
            mx-=1
        my=y+1
        while 0<=my<N:
            
            if grid[x][my]=='S':
                return 1
            elif grid[x][my]=='O':
                break
            my+=1
        my=y-1
        while 0<=my<N:
            
            if grid[x][my]=='S':
                return 1
            elif grid[x][my]=='O':
                break
            my-=1
    return 0

c=combinations(empty,3)
for i in c:
    a,b,c=i[0],i[1],i[2]
    grid[a[0]][a[1]],grid[b[0]][b[1]],grid[c[0]][c[1]]='O','O','O'
    if search()==0:
        print("YES")
        exit()
    grid[a[0]][a[1]],grid[b[0]][b[1]],grid[c[0]][c[1]]='X','X','X'
print("NO")