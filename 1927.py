from queue import PriorityQueue
import sys;input=sys.stdin.readline
N=int(input())
p=PriorityQueue()

for _ in range(N):
    x=int(input())
    if x!=0:
        p.put(x)
    else:
        if p.qsize()==0:
            print(0)
        else:
            print(p.get()) 