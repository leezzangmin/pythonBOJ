import heapq
N=int(input())
sizeOfSlime=list(map(int,input().split()))
heapq.heapify(sizeOfSlime)
score=0
for i in range(N-1):
    a=heapq.heappop(sizeOfSlime)
    b=heapq.heappop(sizeOfSlime)
    score+=(a*b)
    heapq.heappush(sizeOfSlime,a+b)
print(score)