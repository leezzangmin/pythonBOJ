from collections import deque

def solution(priorities, location):
    priorities=deque( list([idx,x] for idx,x in enumerate(priorities)) )
    count=1
    while priorities:
      #  print(priorities,'asdf',count)
        index,element=priorities.popleft()
        flag=True
        temp=[]
        for i,e in priorities:
            if e>element:
                temp.append([index,element])
                flag=False
                break
        for a,b in temp:
            priorities.append([a,b])
        
        if flag:
            if index==location:
                return count
        if flag:
            count+=1


print(solution([2,1,3,2],2))
#print(solution([1, 1, 9, 1, 1, 1],0))