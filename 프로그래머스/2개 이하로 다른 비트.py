def fx(n):
    i=1
    while True:
        temp=n+i
        if bin(n^temp).count('1')<=2:
            return temp
        i+=1

def solution(numbers):
    answer = []
    for i in numbers:
        if i%2==1:
            b=list('0'+bin(i)[2:])
            for j in range(len(b)-1,-1,-1):
                if b[j]=='0':
                    b[j]='1'
                    b[j+1]='0'
                    break
            #"".join(b)
            answer.append(int("".join(b),2))
        else:
            answer.append(fx(i))
    return answer



# 15 -> 01111
# 16 -> 10000
# 17 -> 10001
# 18 -> 10010
# 19 -> 10011
# 20 -> 10100
# 21 -> 10101
# 22 -> 10110
# 23 -> 10111