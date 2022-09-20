def to_binary(number):
    s=""
    while number>0:
        s+=str(number%2)

        number//=2
    return s[::-1]





def solution(n):
    #answer = 0
    one_count=to_binary(n).count('1')
    for i in range(1,1000000):
        if to_binary(n+i).count('1')==one_count:
            return n+i


    #return answer

print(solution(78))
#print(to_binary(78))