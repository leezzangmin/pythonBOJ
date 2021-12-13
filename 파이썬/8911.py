import sys;input=sys.stdin.readline


dx=[0,1,0,-1]
dy=[1,0,-1,0]

T=int(input())
for _ in range(T):
    s=input().rstrip()

    xmin=0
    ymin=0
    xmax=0
    ymax=0
    x,y=0,0
    pointer=0
    ans=0
    for i in s:
        if i=='L':
            pointer-=1
            if pointer==-1:
                pointer=3
        elif i=='R':
            pointer+=1
            if pointer==4:
                pointer=0

        elif i=='F':
            x+=dx[pointer]
            y+=dy[pointer]

        elif i=='B':
            x-=dx[pointer]
            y-=dy[pointer]

        xmin=min(xmin,x)
        ymin=min(ymin,y)
        xmax=max(xmax,x)
        ymax=max(ymax,y)
    
    x=abs(xmin)+abs(xmax)
    y=abs(ymin)+abs(ymax)
    print(x*y)