
def solution(commands):
    answer = []
    N=5
    grid=[['']*N for _ in range(N)]
    pointer=[['']*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            pointer[i][j]=[i,j]


    for c in commands:
        c=c.split(" ")
        if c[0]=="UPDATE":
            if len(c)==4:
                x,y=int(c[1])-1,int(c[2])-1            
                for abc in range(N):
                    for de in range(N):
                        if pointer[abc][de]==[x,y]:
                            grid[abc][de]=c[3]
            else:
                for iiii in range(N):
                    for jjjj in range(N):
                        if grid[iiii][jjjj]==c[1]:
                            grid[iiii][jjjj]=c[2]

        elif c[0]=="MERGE":
            x1,y1,x2,y2=int(c[1])-1,int(c[2])-1,int(c[3])-1,int(c[4])-1
            pointer[x1][y1]=[x1,y1]
            value=grid[x1][y1]
            
            for i in range(abs(x2-x1)+1):
                if x1>x2:
                    xx=x1-i
                else:
                    xx=x1+i
                for j in range(abs(y2-y1)+1):
                    
                    if y1>y2:
                        yy=y1-j
                    else:
                        yy=y1+j
                    grid[xx][yy]=value
                    temp=pointer[xx][yy]

                    pointer[xx][yy]=[x1,y1]

        elif c[0]=="UNMERGE":
            x,y=int(c[1])-1,int(c[2])-1
            for i in range(N):
                for j in range(N):
                    if pointer[i][j]==[x,y]:
                        pointer[i][j]=[i,j]
                        grid[x][y]=grid[i][j]
                        grid[i][j]=''

        elif c[0]=="PRINT":
            # merge 처리필요
            x,y=int(c[1])-1,int(c[2])-1
            x,y=pointer[x][y]
            if grid[x][y]!='':
                answer.append(grid[x][y])
            else:
                answer.append("EMPTY")
        # print(c,'cc')
        # for i in grid:
        #     print(i,'asdf')
        # print()
        # for i in pointer:
        #     print(i,'pointer')


    return answer

print(solution(['UPDATE 1 1 a', 'UPDATE 1 2 b', 'UPDATE 2 1 c', 'UPDATE 2 2 d', 'MERGE 1 1 1 2', 'MERGE 2 2 2 1', 'MERGE 2 1 1 1', 'PRINT 1 1', 'UNMERGE 2 2', 'PRINT 1 1']))