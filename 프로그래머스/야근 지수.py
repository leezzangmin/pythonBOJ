import heapq
def solution(time, works):
    answer = 0
    works=works
    
    for i in range(len(works)):
        works[i]=-works[i]
    heapq.heapify(works)
    while time>0 and works:
        a=heapq.heappop(works)
        if a==0:
            continue
        a+=1
        time-=1
        heapq.heappush(works,a)
    for i in works:
        answer+=i**2

    return answer
print(solution(4,[4,3,3]))