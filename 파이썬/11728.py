import sys;input=sys.stdin.readline
Size_Of_A,Size_Of_B=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=sorted(A+B)
for i in C:
    print(i,end=' ')
print()


