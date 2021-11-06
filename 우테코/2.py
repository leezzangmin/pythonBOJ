def solution(log):
    result=[0,0]
    for i in range(len(log)):
        if i%2==0: #start
            continue
        else:
            temp=timeCalc(log[i-1],log[i])
            if temp[0]>=2: #규칙2
                temp[0]=1
                temp[1]=45
            if temp[0]>=1 and temp[1]>=45: #규칙2
                temp[0]=1
                temp[1]=45

            if temp[0]>=1 or temp[1]>=5: #규칙1
                result[0]+=temp[0]
                result[1]+=temp[1]

    if result[1]>=60:
        while result[1]>=60:
            result[1]-=60
            result[0]+=1
    if result[0]<10:
        answer1='0'+str(result[0])
    else:
        answer1=str(result[0])
    if result[1]<10:
        answer2='0'+str(result[1])
    else:answer2=str(result[1])
    
    answer = answer1+':'+answer2
    return answer

def timeCalc(start,end):
    H=int(end[0:2])-int(start[0:2])
    M=int(end[3:])-int(start[3:])
    if M<0:
        H-=1
        M=abs(M)
    return [H,M]


a=["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11","08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]
b=["01:00", "08:00", "15:00", "15:04", "23:00", "23:59","01:00", "08:00", "15:00", "15:04", "23:00", "23:59","01:00", "08:00", "15:00", "15:04", "23:00", "23:59","01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]
print(solution(b))