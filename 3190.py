from collections import deque;import sys;input=sys.stdin.readline
N=int(input())
grid=[[False]*N for _ in range(N)]
K=int(input())
for _ in range(K):
    temp=list(map(int,input().split()))
    grid[temp[0]-1][temp[1]-1]=True
L=int(input())
direction=[  list(input().split()) for _ in range(L)   ]

snake=deque([[0,0]])
d=['east','south','west','north']
p=0
head=d[p]
time=0

while True:
    if head=='east':
        if 0<=snake[-1][1]+1<N and [snake[-1][0],snake[-1][1]+1] not in snake:
            if grid[snake[-1][0]][snake[-1][1]+1]==True:
                grid[snake[-1][0]][snake[-1][1]+1]=False
                snake.append( [snake[-1][0],snake[-1][1]+1] )
            else:
                snake.append( [snake[-1][0],snake[-1][1]+1] )
                snake.popleft()
        else:
            print(time+1)
            break
        
    elif head=='west':
        if 0<=snake[-1][1]-1<N and [snake[-1][0],snake[-1][1]-1] not in snake:
            if grid[snake[-1][0]][snake[-1][1]-1]==True:
                grid[snake[-1][0]][snake[-1][1]-1]=False
                snake.append( [snake[-1][0],snake[-1][1]-1] )
            else:
                snake.append( [snake[-1][0],snake[-1][1]-1] )
                snake.popleft()
        else:
            print(time+1)
            break

    elif head=='north':
        if 0<=snake[-1][0]-1<N and [snake[-1][0]-1,snake[-1][1]] not in snake:
            if grid[snake[-1][0]-1][snake[-1][1]]==True:
                grid[snake[-1][0]-1][snake[-1][1]]=False
                snake.append( [snake[-1][0]-1,snake[-1][1]] )
            else:
                snake.append( [snake[-1][0]-1,snake[-1][1]] )
                snake.popleft()
        else:
            print(time+1)
            break

    elif head=='south': # south
        if 0<=snake[-1][0]+1<N and [snake[-1][0]+1,snake[-1][1]] not in snake:
            if grid[snake[-1][0]+1][snake[-1][1]]==True:
                grid[snake[-1][0]+1][snake[-1][1]]=False
                snake.append( [snake[-1][0]+1,snake[-1][1]] )
            else:
                snake.append( [snake[-1][0]+1,snake[-1][1]] )
                snake.popleft()
        else:
            print(time+1)
            break

    time+=1 
    for i in direction:
        if time==int(i[0]):
            if i[1]=='L':
                p-=1
                if p<0:
                    p=3
                head=d[p]
            else: #'D
                p+=1
                if p>3:
                    p=0
                head=d[p]
           
