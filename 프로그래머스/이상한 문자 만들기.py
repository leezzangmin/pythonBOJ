def solution(s):
    s=s.lower()
    answer = ''

    count=0
    for i in range(len(s)):
        if s[i] == ' ':
            count=0
            answer+=' '
            continue
        if count%2 == 0:
            answer += s[i].upper()
        else:
            answer+=s[i]
        count+=1
    
    return answer
s="try hello world"	
solution(s)