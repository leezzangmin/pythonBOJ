from itertools import permutations

def solution(k, dungeons):
    answer = -1
    p=permutations(dungeons,len(dungeons))
    for i in p:
        temp_k=k
        count=0
        for least,spent in i:
            if least<=temp_k:
                temp_k-=spent
                count+=1
        answer=max(count,answer)
    return answer



print(solution(80,[[80,20],[50,40],[30,10]]))
