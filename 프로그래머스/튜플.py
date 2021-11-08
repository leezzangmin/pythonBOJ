def solution(s):
    temp=[]
    temp2=''
    count=0
    for i in range(len(s)):
        if s[i]=="{":
            continue
        elif s[i]=="}":
            if temp2!='':
                print(temp2,'asdf')
                temp2=temp2.split(',')
                print(temp)
            continue
        elif s[i]==",":
            if s[i+1]=="{":
                continue
            else:
                temp2+=s[i]
        else:
            temp2+=s[i]
            count+=1


    answer = []
    return answer


s="{{20,111},{111}}"
solution(s)