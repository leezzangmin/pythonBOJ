def solution(answers):
    answer = []

    number1=[1,2,3,4,5]
    number2=[2,1,2,3,2,4,2,5]
    number3=[3,3,1,1,2,2,4,4,5,5]

    temp_score=0
    score=0

    j=0
    for i in range(len(answers)):
        if j==len(number1):
            j=j%len(number1)
        if answers[i]==number1[j]:
            temp_score+=1
        j+=1

    score=temp_score
    answer=[1]



    temp_score=0
    j=0
    for i in range(len(answers)):
        if j==len(number2):
            j=j%len(number2)
        if answers[i]==number2[j]:
            temp_score+=1
        j+=1
    if temp_score==score:
        answer.append(2)
    elif temp_score>score:
        score=temp_score
        answer=[2]
    


    temp_score=0
    j=0
    for i in range(len(answers)):
        if j==len(number3):
            j=j%len(number3)
        if answers[i]==number3[j]:
            temp_score+=1
        j+=1
    
    if temp_score==score:
        answer.append(3)
    elif temp_score>score:
        answer=[3]
    return answer

a=[1,3,2,4,2]	
print(solution(a))