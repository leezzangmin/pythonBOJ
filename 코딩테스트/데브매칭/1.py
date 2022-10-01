import sys;
sys.setrecursionlimit(10**7)
from collections import deque

def solution(registered_list, new_id):

    if new_id not in registered_list:
        return new_id
    S,N='',''
    ln=len(new_id)
    i=0
    while i!=ln:
        if not new_id[i].isalpha():
            S=new_id[0:i]
            N=int(new_id[i:])
            break
        i+=1
    
    if i==ln:
        S=new_id
        N=0

    Q=deque()
    for i in range(len(registered_list)):
        if not registered_list[i].startswith(S):
            Q.append(i)
    
    while Q:
        x=Q.pop()
        del registered_list[x]

    registered_list.sort()

    lr=len(registered_list)
    numbers=[-1]*lr
    ls=len(S)
    for i in range(lr):
        a=0
        try:
            a=int(registered_list[i][ls:])
            if a!=0:
                numbers[i]=a
        except:
            continue
        
    numbers.sort()
    print(numbers,'nubmers')
    if N==0:
        N=1
    print(S,N,"SNSN")
    ln=len(numbers)
    pointer=0
    for i in range(ln):
        if i!=-1:
            temp=numbers[i]
            pointer=i
            break
    print(temp,'temp')
    for i in range(pointer+1,len(numbers)):
        if temp+1!=numbers[i]:
            return S+str(temp+1)
        else:
            temp=numbers[i]
        
    



    return S+str(N)

solution([],"ace")
