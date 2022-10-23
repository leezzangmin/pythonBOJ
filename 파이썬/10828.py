import sys;input=sys.stdin.readline
N=int(input())

stack=[]
s=0
for _ in range(N):
    i=input().rstrip().split()
    if i[0]=='push':
        stack.append(i[1])
        s+=1
    elif i[0]=='pop':
        if s!=0:
            print(stack.pop())
            s-=1
        else:
            print(-1)
    elif i[0]=='size':
        print(s)
    elif i[0]=='empty':
        if s==0:
            print(1)
        else:
            print(0)
    elif i[0]=='top':
        if s==0:
            print(-1)
        else:
            print(stack[-1])