from collections import deque
def define(modified,length):
    stack=['x']
    for _ in range(length):
        i=modified.popleft()
        if i=='[':
            if stack[-1]==']':
                stack.pop()
        elif i=='{':
            if stack[-1]=='}':
                stack.pop()
        elif i=='(':
            if stack[-1]==')':
                stack.pop()
        else:
            stack.append(i)
    print(stack)
    
    if len(stack)==1:
        return True
    else:
        return False

def solution(s):
    answer = 0
    s=deque(list(s))
    ls=len(s)
    for _ in range(ls):
        if define(s,ls):
            answer+=1
        s=s.rotate(1)
    print(s)

    return answer