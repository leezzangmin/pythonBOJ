from collections import deque

def solution(new_id):
    answer = list(new_id.lower())
    ln=len(new_id)
    #new_id=new_id.lower()
    giho=['-','_','.']
    Q=deque()
    for i in range(ln):
        if not (answer[i].isalnum() or answer[i] in giho):
            Q.append(i)
        
    lq=len(Q)
    for i in range(lq):
        x=Q.pop()
        del answer[x]
    #print("".join(answer),'answer')


    la=len(answer)
    for i in range(la):
        if answer[i]=='.' and i+1!=la and answer[i+1]=='.':
            Q.append(i)
    lq=len(Q)
    for i in range(lq):
        x=Q.pop()
        del answer[x]
    
   # print("".join(answer),'answer')

    la=len(answer)
    if la!=0 and answer[-1]=='.':
        del answer[-1]
        la-=1
    if la!=0 and answer[0]=='.':
        del answer[0]
        la-=1
    
    if la==0:
        answer.append('a')
        la+=1
    if la>=16:
        answer=answer[0:15]
        la=15
        if answer[-1]=='.':
            del answer[-1]
            la=14
    if la<=2:
        while len(answer)!=3:
            answer.append(answer[-1])
    


    
    return "".join(answer)

#print(solution("...!@BaT#*..y.abcdefghijklm"))
a="abcdefghijklmn.p"
a=a[0:15]
print(a)
