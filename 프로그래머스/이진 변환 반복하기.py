def solution(s):
    answer = [0,0]
    while int(s,2)!=1:
        ls=0
        zero_count=0
        for i in s:
            if i=='0':
                zero_count+=1
            else:
                ls+=1
        
        s=bin(ls)[2:]
        answer[1]+=zero_count
        answer[0]+=1
    
    
    return answer
print(solution('1111111'))