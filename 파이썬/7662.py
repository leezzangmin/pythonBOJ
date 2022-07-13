import sys;input=sys.stdin.readline
import heapq
T=int(input())
g=0
for _ in range(T):

    k=int(input())
    maxHeap=[]
    minHeap=[]
    count=0
    trash=[]
    for _ in range(k):
        c,n=input().split();n=int(n)
        if c=='I':
            count+=1
            heapq.heappush(minHeap,(n,g))
            heapq.heappush(maxHeap,(-n,g))
            g+=1
        else: # c=='D'
            if count>0:
                count-=1
            else:
                minHeap=[]
                maxHeap=[]
                trash=[]
                continue

            if n==1: #최댓값 삭제
                num,glo=heapq.heappop(maxHeap)
                while (-num,glo) in trash:
                    num,glo=heapq.heappop()
                trash.append((-num,glo))
            else:    #최솟값 삭제
                num,glo=heapq.heappop(minHeap)
                while (num,glo) in trash:
                    num,glo=heapq.heappop()
                trash.append((num,glo))
            
    if len(maxHeap)==0 or len(minHeap)==0:
        print("EMPTY")
    else:
        print(-heapq.heappop(maxHeap)[0],heapq.heappop(minHeap)[0])
# 1
# 12
# I -1
# I -2
# I 1
# I 10
# I 2
# I 3
# I 4
# I 5
# I 6
# I 7
# I 8
# D 1

