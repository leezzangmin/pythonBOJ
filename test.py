import heapq

answer = 0
priorities=[3,2,1,1234]
priorities=priorities*-1
print(priorities,'dd')
a=heapq.heapify(priorities)

print(heapq.heappop(priorities),'asdf')
print(heapq.heappop(priorities),'asdf')
print(heapq.heappop(priorities),'asdf')
print(heapq.heappop(priorities),'asdf')