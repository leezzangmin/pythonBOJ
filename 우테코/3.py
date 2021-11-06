def solution(ings, menu, sell):
    answer = 0
    gredient=[0]*26
    for i in ings:
        gredient[ord(i[0])-97]=int(i[2:])

    food=[]
    for i in menu:
        a=i.split()
        onega=0
        for j in a[1]:
            onega+=gredient[ord(j)-97]
        food.append([a[0],int(a[2])-onega])


    for i in sell:
        a=i.split()
        for j in range(len(food)):
            if a[0]==food[j][0]:
                answer+= food[j][1]*int(a[1])


    return answer

a=["r 10", "a 23", "t 124", "k 9"]	
b=["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"]	
c=["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]
d=["x 25", "y 20", "z 1000"]	
e=["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"]	
f=["BBBB 3", "TTT 2"]
print(solution(a,b,c))