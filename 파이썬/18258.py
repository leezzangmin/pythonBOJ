from collections import deque
import sys;input=sys.stdin.readline
N=int(input())
q=deque()

for i in range(N):
    s=input().rstrip()
    if s[0:3]=='pus':
        q.append(int(s[5:]))
    elif s[0:3]=='pop':
        try:
            print(q.popleft())
        except:
            print(-1)
    elif s[0:3]=='siz':
        print(len(q))
    elif s[0:3]=='emp':
        try:
            q[0]
            print(0)
        except:
            print(1)
    elif s[0:3]=='fro':
        try:
            print(q[0])
        except:
            print(-1)
    elif s[0:3]=='bac':
        try:
            print(q[-1])
        except:
            print(-1)