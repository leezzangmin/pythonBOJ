import sys;input=sys.stdin.readline
T=int(input())

for _ in range(T):
    commands=list(input().rstrip())
    s1=list()
    s2=list()
    for i in commands:
        if i=="<":
            if s1:
                s2.append(s1.pop())
        elif i==">":
            if s2:
                s1.append(s2.pop())
        elif i=="-":
            if s1:
                s1.pop()   
        else:
            s1.append(i)
    s2.reverse()
    print("".join(s1+s2))
