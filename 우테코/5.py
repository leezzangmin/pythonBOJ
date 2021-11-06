def solution(rows, columns):
    answer = [[]]
    global grid
    grid=[[0]*columns for _ in range(rows)]
    visit=[[0]*columns for _ in range(rows)]
    cur=1
    r,c=0,0
    while isGood():
        grid[r][c]=cur
        visit[r][c]=cur
        if cur%2==0:
            if r==rows-1:
                r=0
            else:
                r+=1

        elif cur%2==1:
            if c==columns-1:
                c=0
            else:
                c+=1
        if visit[r][c]!=0 :
            if (visit[r][c]%2==(cur+1)%2):
                return grid
            
        grid[r][c]=cur+1
        cur+=1

    return grid

def isGood():
    for i in grid:
        for j in i:
            if j==0:
                return True
    return False


a=solution(20,2)
for i in a:
    print(i)
