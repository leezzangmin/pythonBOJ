def solution(s):
    answer = []
    while s[0]==s[-1]:
        s=s[-1]+s[0:len(s)-1]

    count=1
    first=s[0]
    for i in range(1,len(s)):
        if s[i]==first:
            count+=1
        else:
            answer.append(count)
            count=1
            first=s[i]
    answer.append(count)
    answer.sort()



    return answer


a="aaabbaaa"
b="wowwow"
c="bbcabb"
d="ABCDAAAA"
solution(d)