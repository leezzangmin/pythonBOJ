


def solution(lottos, win_nums):
    least=lottos.count(0)
    rate=[6,6,5,4,3,2,1]
    temp=0
    for i in lottos:
        if i in win_nums:
            temp+=1

    
    answer = [rate[least+temp],rate[temp]]
    return answer

if __name__=="__main__":
    a=[45, 4, 35, 20, 3, 9]	
    b=[20, 9, 3, 45, 4, 35]
    print(solution(a,b))

