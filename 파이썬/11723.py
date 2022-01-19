import sys;input=sys.stdin.readline
M=int(input())
bit=[False]*21
ans=[]
for _ in range(M):
    s=input().rstrip().split()
    if s[0][0:2]=='ad':
        bit[int(s[1])]=True
    elif s[0][0]=='r':
        bit[int(s[1])]=False
    elif s[0][0]=='c':
        if bit[int(s[1])]==True:
            print(1)
        else:
            print(0)
    elif s[0][0]=='t':
        bit[int(s[1])] = not bit[int(s[1])]
    elif s[0][0:2]=='al':
        bit=[True]*21
    elif s[0][0]=='e':
        bit=[False]*21
