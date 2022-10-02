

def combination(N, M, level, idx):
    if level == M:
        print(result)
        return

    for i in range(idx, N):
        result[level] = list[i]
        combination(N, M, level + 1, i + 1) # i+1 말고 i면 중복 허용

def solution(k):
    answer=0    

    fire=[6,2,5,5,4,5,6,3,7,6]

    if k==1:
        return 0
    #elif k==5:
    #    return 5
    #elif k==6:
    #    return 7
   # elif k==11:
  #     return 99
    
    for i in range(11,-1,-1):
        if k>fire[i]:
            k-=1


    

    
    return answer
solution(50)