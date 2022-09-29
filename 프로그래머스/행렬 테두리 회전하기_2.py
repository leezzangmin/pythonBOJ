from collections import deque


def solution(rows, columns, queries):
    answer = []
    grid = [ list(i+j for i in range(columns)) for j in range(1,columns*rows+1,columns) ]
    for i in grid:
        print(i)
    
    for x1,y1,x2,y2 in queries:
        x1-=1;y1-=1;x2-=1;y2-=1
        Q=deque()
        print(x1,y1,x2,y2,'query')
        for y in range(y1,y2+1):
            Q.append(grid[x1][y])
        for x in range(x1+1,x2):
            Q.append(grid[x][y2])
        for y in range(y2,y1-1,-1):
            Q.append(grid[x2][y])
        for x in range(x2-1,x1,-1):
            Q.append(grid[x][y1])
        #Q.append(Q.popleft())
        Q.rotate()
        answer.append(min(Q))
        for y in range(y1,y2+1):
            grid[x1][y]=Q.popleft()
            #Q.append(grid[x1][y])
        for x in range(x1+1,x2):
            grid[x][y2]=Q.popleft()
            #Q.append()
        for y in range(y2,y1-1,-1):
            grid[x2][y]=Q.popleft()
            #Q.append()
        for x in range(x2-1,x1,-1):
            grid[x][y1]=Q.popleft()
            #Q.append()
        for i in grid:
            print(i)





    return answer


# 최대 400만




print(solution(100,97,[[1,1,100,97]]	))