from typing import List
from collections import defaultdict
# http://2022line-test.channel.io

# 새로운 배열의 크기는 원소의  수 이상인 2의 거듭제곱 중에서 가장 작은 값
# 원소가 복사된 갯수를 return (복사된 횟수가 아니라 복사된 원소의 갯수)
# d[1]=[1,2] #size, element_count

def define_size(asdf):
    i=1
    while i<asdf:
        i*=2
    return i

def solution(queries: List[List[int]]) -> int:
    answer = 0
    d=defaultdict()
    lq=len(queries)
    for i in range(lq):
        arr_num, ele_cnt=queries[i]
      #  if i>=1:print(d[arr_num],'asdfasdf')
        if arr_num in d:
            if d[arr_num][0]<d[arr_num][1]+ele_cnt:
                answer+=d[arr_num][1]
              #  print(answer,'asdf',arr_num,ele_cnt,d[arr_num][1])
                new_size=define_size(d[arr_num][1]+ele_cnt)
                d[arr_num][0]=new_size
                d[arr_num][1]=d[arr_num][1]+ele_cnt
            else: #d[arr_num][0]>=d[arr_num][1]+ele_cnt:
                d[arr_num][1]=d[arr_num][1]+ele_cnt

        else: # arr_num not in d:
            d[arr_num]=[define_size(ele_cnt)]
            d[arr_num].append(ele_cnt)

   # print(d,'dddddddddddd')
    return answer

#print(solution([[1,1],[1,2]]))
print(solution([[1,1],[1,3],[1,4],[1,5],[1,1],[1,1],[1,1],[1,0]]))
#print(define_size(1025))