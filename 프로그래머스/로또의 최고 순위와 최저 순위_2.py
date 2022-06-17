def solution(lottos, win_nums):
    win={6:1,5:2,4:3,3:4,2:5,1:6,0:6}

    M=lottos.count(0)
    win_count=0
    for i in lottos:
        if i in win_nums:
            win_count+=1
    
    return [win[win_count+M],win[win_count]]


#print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))