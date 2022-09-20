def solution(prices):
    lp=len(prices)
    answer = [0]*lp
    for i in range(lp):
        temp=0
        for j in range(i,lp):
            if prices[i]>prices[j]:
                answer[i]=temp
                break
            temp+=1
        if answer[i]==0:
            answer[i]=temp-1


    return answer
solution([1,2,3,2,3])