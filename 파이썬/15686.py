import sys;
input=sys.stdin.readline
from itertools import combinations
#0은 빈 칸, 1은 집, 2는 치킨집이다.

def dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)


if __name__=="__main__":
    N,M=map(int,input().split())
    city=list(list(map(int,input().split())) for _ in range(N))
    house=[]
    chicken=[]
    for i in range(N):
        for j in range(N):
            if city[i][j]==0:
                continue
            if city[i][j]==1:
                house.append((i,j))
                continue
            if city[i][j]==2:
                chicken.append((i,j))
    
    ans=sys.maxsize
    for xy in combinations(chicken,M):
        #for i,j in xy:  # (4,0) (1,1)
        temp=0
        for x1,y1 in house:
            temp+= min(dist(x1,y1,x2,y2) for x2,y2 in xy)
            if temp>ans:
                break
        ans=min(temp,ans)
    print(ans)
