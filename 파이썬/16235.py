# 양분은 모든 칸에 5만큼 들어있다.
# 같은 1×1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다.

# 봄
# 자신의 나이만큼 양분을 먹
# 어린놈부터 먹음

#여름
# 여름에는 봄에 죽은 나무가 양분으로 변하게 된다. 
# 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다.
#  소수점 아래는 버린다.

#가을 - 번식
# 나무 나이 5의배수, 인접한 8개칸 나이 1인나무가 하나 생김

#겨울 - 양분추가
# A[r][c]만큼 각 칸에 추가
import sys;input=sys.stdin.readline
import heapq
N,M,K=map(int,input().split())
dx=[0,0,1,-1,-1,1,-1,1]
dy=[1,-1,0,0,-1,-1,1,1]

A=list(list(map(int,input().split())) for _ in range(N))
yangboon=[[5]*N for _ in range(N)]
treecount=dict()
for _ in range(M):
    tree_x,tree_y,age = map(int,input().split())
    if treecount.get((tree_x-1,tree_y-1)):
        heapq.heappush(treecount.get((tree_x-1,tree_y-1)),age)
    else:
        treecount[(tree_x-1,tree_y-1)]=[age]

for _ in range(K):
    dead=[]
    alive=dict()
    for i in treecount:
        while treecount[i]:
            temp=list(treecount[i])
            youngTreeAge=heapq.heappop(treecount[i])
            curY=yangboon[i[0]][i[1]]
            if curY>=youngTreeAge:
                yangboon[i[0]][i[1]]-=youngTreeAge
                if alive.get(i):
                    alive[i].append(youngTreeAge+1)
                else:
                    alive[i]=[youngTreeAge+1]
            else:
                dead.append((i,youngTreeAge//2))

    for xy in alive:
        agelist=alive[xy]
        if type(agelist)==int:
            treecount[(xy[0],xy[1])]=[agelist]
        else:
            heapq.heapify(agelist)
            #agelist.reverse()
            treecount[(xy[0],xy[1])]=agelist

    for xy,age in dead:
        yangboon[xy[0]][xy[1]]+=age
    young=[]
    reAppend=dict()
    for i in treecount:
        for j in range(len(treecount[i])):
            age=heapq.heappop(treecount[i])
            if reAppend.get(i):
                reAppend[i].append(age)
            else:
                reAppend[i]=[age]
            #reAppend.append((i,age))
            x=i[0]
            y=i[1]
            if age%5==0:
                for asdf in range(8):
                    mx=x+dx[asdf]
                    my=y+dy[asdf]
                    if 0<=mx<N and 0<=my<N:
                        young.append((mx,my))
    for xy in reAppend:
        age=reAppend[xy]
        if type(age)==int:
            treecount[xy]=[age]
        else:
            heapq.heapify(age)
            treecount[(xy[0],xy[1])]=age
        
    for mx,my in young:
        if treecount.get((mx,my)):
            heapq.heappush(treecount[(mx,my)],1)
        else:
            treecount[(mx,my)]=[1]

    for i in range(N):
        for j in range(N):
            yangboon[i][j]+=A[i][j]
ans=0            
for i in treecount.values():
    if type(i)==list:
        ans+=len(i)
    else:
        ans+=1
print(ans)