import heapq
n,m=map(int,input().split())
cards=list(map(int,input().split()))

# cards=[]
# for i in range(n):
#     heapq.heappush(cards,card[i])

heapq.heapify(cards)

for i in range(m):
    a=heapq.heappop(cards)
    b=heapq.heappop(cards)
    c=a+b
    heapq.heappush(cards,c)
    heapq.heappush(cards,c)
print(sum(cards))