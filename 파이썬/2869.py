import math
A,B,V=map(int,input().split())
ans=0
C=A-B
print(math.ceil((V-B) / C))