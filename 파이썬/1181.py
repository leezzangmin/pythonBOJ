import sys;input=sys.stdin.readline;N=int(input())
for i in sorted( list(set(input().rstrip() for _ in range(N))),key=lambda x:(len(x),x)):print(i)