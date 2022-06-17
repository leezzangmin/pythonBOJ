import sys;input=sys.stdin.readline

N,M,R=map(int,input().split())
grid= list( list(map(int,input().split())) for _ in range(N))


def rotate(x,y):
    global temp
    global grid
    # 1번라인
    for up in range(x,M-x-1): #0,4 -> 1,3
        temp[x][up]=grid[x][up+1]
    
    #마지막라인
    for down in range(M-x-1,x,-1):
        temp[N-1-x][down]=grid[N-1-x][down-1]
    #왼
    for left in range(y,N-y-1):
        temp[left+1][y]=grid[left][y]
    #오
    for right in range(y,N-y-1):
        temp[right][M-1-y]=grid[right+1][M-1-y]


for _ in range(R):
    ii,jj=0,0
    temp= list( [0] * M for _ in range(N))
    for _ in range(int(min(N,M)/2)):
        rotate(ii,jj)
        ii+=1;jj+=1


    grid=temp
for i in grid:
    for j in i:
        print(j,end=' ')
    print()