def solution(s):
    answer = []
    s=s.split(" ")
    ls=len(s)
    for i in range(ls):
        temp=''
        if s[i]=='':
            answer.append(' ')
            continue
        for j in range(len(s[i])):
            if j==0:
                if s[i][j].isdigit():
                    temp+=s[i][j]
                else:
                    #print(s[i][j].upper(),'upper')
                    temp+=s[i][j].upper()
            else:
                temp+=s[i][j:].lower()
                break
        answer.append(temp)
    a=''
    for i in answer:
        if i==' ':
            a+=' '
        else:
            a+=i+' '
    #answer="".join(answer)
    return a

print(solution("3people  unFollowed me"))