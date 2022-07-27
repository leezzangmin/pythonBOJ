from collections import deque
import sys;input=sys.stdin.readline
def D(n):
    n=n*2
    if n>9999:
        return n%10000
    return n
def S(n):
    n-=1
    if n==-1:
        return 9999
    return n
def L(n):

    return ( 10 * n + (n //1000) ) % 10000


def R(n):

    return ((n%10)*1000 + n//10) %10000
    
T=int(input())
for _ in range(T):
    
    visit=[False]*10000
    A,B=map(int,input().split())
    visit[A]=True
    Q=deque()
    Q.append((A,""))
    while Q:
        num,path=Q.popleft()
        if num==B:
            print(path)
            break

        num2=D(num)
        if visit[num2]==False:
            visit[num2]=True
            Q.append((num2,path+"D"))
        
        num2=S(num)
        if visit[num2]==False:
            visit[num2]=True
            Q.append((num2,path+"S"))



        num2=L(num)
        if visit[num2]==False:
            visit[num2]=True
            Q.append((num2,path+"L"))

        num2=R(num)
        if visit[num2]==False:
            visit[num2]=True
            Q.append((num2,path+"R"))
