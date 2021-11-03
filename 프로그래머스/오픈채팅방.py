def solution(record):
    answer = []

    dic={}
    message=[]
    for i in record:
        a=i.split()
        if i[0]=='E':
            message.append((0,a[1]))
            dic[a[1]]=a[2]
        elif i[0]=='L':
            message.append((1,a[1]))
        elif i[0]=='C':
            dic[a[1]]=a[2]

    for i in message:
        if i[0]==0:
            answer.append(str(dic[i[1]])+'님이 들어왔습니다.')
        elif i[0]==1:
            answer.append(str(dic[i[1]])+'님이 나갔습니다.')

    return answer


r=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(r)