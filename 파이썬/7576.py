

def dfs(x,y):
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if 0<=mx<N and 0<=my<M:
            if box[mx][my]==0:
                box[mx][my]=box[x][y]+1
                idx.append((mx,my))

def isGood():
    for i in box:
        if 0 in i:
            return False
    return True

if __name__=="__main__":
    import sys;input=sys.stdin.readline
    import copy
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    M,N=map(int,input().split())
    box=list(list(map(int,input().split()))for _ in range(N))

    idx=[]
    for i in range(N):
        for j in range(M):
            if box[i][j]==1:
                idx.append((i,j))

    ans=0
    while isGood()==False:
        box2=copy.deepcopy(box)
        for a,b in idx:
            dfs(a,b)
        idx=[]
        
        if box2==box:
            ans=-1
            break
    if ans==-1:
        print(ans)
    else:
        print(max(map(max, box))-1)
    
                
