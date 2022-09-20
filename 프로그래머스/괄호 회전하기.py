from collections import deque
def define(modified,length):
    stack=['x']
   # print(modified,'modi')
    for i in modified:
        if i==']':
            if stack[-1]=='[':
                stack.pop()
            else:
                stack.append(i)
        elif i=='}':
            if stack[-1]=='{':
                stack.pop()
            else:
                stack.append(i)
        elif i==')':
            if stack[-1]=='(':
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
  #  print(stack)
    
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
        s.rotate(1)
    print(answer)

    return answer