import sys;input=sys.stdin.readline
N,d,k,c=map(int,input().split())
sushi=list(int(input()) for _ in range(N))

print(sushi)
L,R=0,1
link=[sushi[L]]

while L!=N-k+1:
    if len(link)==k:
        print(link)
        L+=1
        R=L+1
        link=[sushi[L]]
    if sushi[R] in link:
        L+=1
        R=L+1
        link=[sushi[L]]
    else:
        link.append(sushi[R])
        R+=1
