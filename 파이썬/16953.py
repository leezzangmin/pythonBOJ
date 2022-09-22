from collections import deque
A,B=map(int,input().split())
#visit=[False]*(B+1)

Q=deque()
Q.append((A,0))
while Q:
   # print(Q,'QQ')
    x,count=Q.popleft()
    if x==B:
        #print(Q,'QQ')
        print(count+1)
        exit()
   # visit[x]=True
    x1=int(str(x)+'1')
    x2=x*2
    if x1<=B:# and visit[x1]==False:
        Q.append((x1,count+1))
    if x2<=B:# and visit[x2]==False:
        Q.append((x2,count+1))

print(-1)