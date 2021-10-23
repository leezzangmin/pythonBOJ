import sys;input=sys.stdin.readline;import heapq
N=int(input())


s=[]
for i in range(N):
    a=int(input())
    if a!=0:
        heapq.heappush(s,(abs(a),a))
    else:
        if not s:
            print(0)
        else:
            print(heapq.heappop(s)[1])
