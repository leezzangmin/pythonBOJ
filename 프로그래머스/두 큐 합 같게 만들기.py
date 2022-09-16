from collections import deque
def solution(queue1, queue2):
    answer = -1
    s=sum(queue1)+sum(queue2)
    h=int(s/2)
    if (s % 2) == 1:
        return answer
    
    answer=0
    q1s=sum(queue1)
    q2s=sum(queue2)
    queue1,queue2=deque(queue1),deque(queue2)
    
    for i in range(len(queue1)*4):
        if q1s<q2s:
            p=queue2.popleft()
            q2s-=p
            q1s+=p
            queue1.append(p)
        elif q1s>q2s:
            p=queue1.popleft()
            q1s-=p
            q2s+=p
            queue2.append(p)
        else:
            return answer
        answer+=1
    
    
    return -1