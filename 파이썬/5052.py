import sys;input=sys.stdin.readline
T=int(input())

for _ in range(T):
    N=int(input())
    s=sorted([input().rstrip() for _ in range(N)])
    flag=False

    for i in range(len(s)-1):
        if s[i]==s[i+1][0:len(s[i])]:
            flag=True
            break
    if flag:
        print('NO')
    else:
        print('YES')

