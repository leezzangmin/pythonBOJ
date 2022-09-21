def min_UpDown(c1,c2):
    # a=65 z=90
    # j=74
    r=ord(c2)-ord(c1)
    for i in range(1,25):
        temp=ord(c1)-i
        if temp<65:
            temp+=26
        if chr(temp)==c2:
            r=min(r,i)
            break
    return r

def min_cursor(current,target,length):
    r=abs(target-current)
    for i in range(1,length-1):
        temp=cur-i
        if temp<0:
            temp=length+temp
            if temp==target:
                r=min(r,i)
                break
    return r
    
def solution(name):
    #JAAAAZZ
    #JJJAAAAAAAAAZ - 0 1 2 9
    answer = 0
    targets=[]
    ln=len(name)
    for i in range(ln):
        if name[i]!='A':
            answer+=min_UpDown('A',name[i])
            targets.append(i)
    print(targets,'targets')
    visit=[False]*ln            
    if 'A' not in name:
        answer+=ln-1
    else:
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min(min_move, i + i + len(name) - next)       
        answer+=min_move
    return answer