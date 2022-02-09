import sys; input=sys.stdin.readline
from collections import deque
F,S,G,U,D=map(int,input().split())
D=-D

building = [0]*(F+1)

def bfs():
    Q=deque()
    Q.append(S)
    building[S]=1
    while Q:
        floor=Q.popleft()
        if floor==G:
            return building[floor]-1
        for mfloor in (floor+U,floor+D):
            if 0<mfloor<=F and building[mfloor]==0:
                building[mfloor]=building[floor]+1
                Q.append(mfloor)
    return "use the stairs"

print(bfs())
#print(building)
