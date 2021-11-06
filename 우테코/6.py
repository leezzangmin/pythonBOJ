def solution(time, plans):
    for i in plans:
        temp=0
        i[1]=timeModify(i[1])
        i[2]=timeModify(i[2])
        if 18>i[1]:
            if i[1]<=9:
                temp+=18-9.5 # 금요일 일차
            else:
                temp+=18-i[1] # 금요일 반 ~ 일차

        if time>temp:
            if 13<i[2]:
                if i[2]>18:  #월요일 일차
                    temp+=5
                else:
                    temp+=i[2]-13 #월요일 반차
        

        if temp<=time:
            time-=temp
            answer=i[0]


    return answer



def timeModify(s):
    if s[-2]=='P':
        if len(s)==3:
            s=int(s[0])+12
        elif len(s)==4:
            s=int(s[0:2])+12
    elif s[-2]=='A':
        if len(s)==3:
            s=int(s[0])
        elif len(s)==4:
            s=int(s[0:2])
    return s


a=4
b=[ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ]
print(solution(a,b))