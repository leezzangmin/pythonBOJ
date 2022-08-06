def sero_destroyable(y):
    print(y,'asdf')
    global temp_grid
    global Q
    temp_count=0
    ans=False
    for i in range(N):
        if temp_grid[i][y]!=0:
            temp_count+=1
    print(temp_count)
    for i in range(N):
        if temp_count!=0 and temp_grid[i][y]==temp_count:
            ans=True
            Q.append((i,y))
    return ans
def down(yyy):
    global temp_grid
    for i in range(N-1,0,-1):
        temp_grid[i][yyy]=temp_grid[i-1][yyy]
    temp_grid[0][yyy]=0

from collections import deque
Q=deque()
N=7

temp_grid=[
[0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 2, 0],
[0, 0, 0, 0, 0, 7, 0],
[0, 0, 0, 0, 4, 4, 0],
[0, 0, 0, 0, 1, 5, 0],
[0, 0, 0, 4, 2, 6, 0],
[3, 3, 3, 5, 5, 7, 1]]
down(5)
for i in temp_grid:
    print(i)