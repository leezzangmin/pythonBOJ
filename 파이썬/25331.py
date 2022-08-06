import sys;input=sys.stdin.readline
from collections import deque
import copy;import time
N=7
gryd=[[0,0,0,0,0,0,0]]
input()
for i in range(N-1):
    temp=list(map(int,input().split()))
    gryd.append(temp)
ball=int(input())

def garo_destroyable():
    global temp_grid
    global Q
    ans=False

    for i in range(N):
        size=0
        for j in range(N):
            if temp_grid[i][j]!=0:
                size+=1
            else:
                if size!=0:
                    for k in range(j-1-size,j):
                        if temp_grid[i][k]==size:
                            ans=True
                            Q.append((i,k))
                size=0
        if size!=0:
            for k in range(N-size,N):
                if temp_grid[i][k]==size:
                    ans=True
                    Q.append((i,k))
   
    return ans
        
def sero_destroyable():
    global temp_grid
    global Q
    
    ans=False
    for cd in range(N):
        temp_count=0
        for i in range(N):
            if temp_grid[i][cd]!=0:
                temp_count+=1
        for j in range(N):
            if temp_count!=0 and temp_grid[j][cd]==temp_count:
                ans=True
                Q.append((j,cd))
    return ans

def down(xxx,yyy):
    global temp_grid
    for i in range(xxx,0,-1):
        temp_grid[i][yyy]=temp_grid[i-1][yyy]
    temp_grid[0][yyy]=0

answer=1
for i in range(N):
    for j in range(N):
        if gryd[i][j]!=0:
            answer+=1
answer=min(43,answer)
for j in range(N):
    for i in range(N-1,-1,-1):
        if gryd[i][j]==0:
            
            Q=list()
            temp_grid=copy.deepcopy(gryd)
            temp_grid[i][j]=ball
            garoflag=garo_destroyable()
            seroflag=sero_destroyable()
            while seroflag or garoflag:
                Q=list(set(Q))
                Q.sort(key=lambda x:x[0],reverse=True)                
             #   print(Q,'asdf',i,j)

                
                while Q:
                    xx,yy=Q.pop()
                    down(xx,yy)               
                garoflag=garo_destroyable()
                seroflag=sero_destroyable()

            t=0
            for i in range(N):
                for j in range(N):
                    if temp_grid[i][j]!=0:                
                        t+=1
            answer=min(answer,t)


            break

print(answer)

