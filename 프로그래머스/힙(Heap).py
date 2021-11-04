#섞은 음식의 스코빌 지수 = 
#가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count=0
    a=heapq.heappop(scoville)
    heapq.heappush(scoville,a)
    while a<K:
        a=heapq.heappop(scoville)

        if a>=K:
            break
        try:
            b=heapq.heappop(scoville)
        except:
            return -1
        heapq.heappush(scoville,a+(b*2))
        count+=1
        
    answer = count

    return answer

s=[1, 2, 3, 9, 10, 12]	
K=7
solution(s,K)