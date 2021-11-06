# 정수 1, 2, 3을 담고 있는 배열이 주어집니다. 
# 이 배열에 원소를 추가해서 배열 안의 1, 2, 3의 개수가 모두 같아지도록 하려 합니다. 
# 단, 추가하는 원소의 개수는 최소가 되어야 합니다.

def solution(arr):
    num=[0]*(max(arr)+1)
    for i in range(len(arr)):
        num[arr[i]] +=1

    n=max(num)
    answer = [0,0,0]
    for i in range(1,len(num)):
        if num[i]<3:
            answer[i-1]+=n-num[i]

    return answer


solution([1, 2, 3])