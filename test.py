import heapq
h=[]
heapq.heappush(h,(-1,123))
heapq.heappush(h,(-1,124))

print(heapq.heappop(h))