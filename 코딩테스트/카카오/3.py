# 1. 서비스가입자
# 2. 판매액

# 이진탐색?

#비율 1<= x <=40
#할인율은 10% 20% 30% 40% 

import sys
def solution(users, emoticons):
    answer = [0,0]
    le=len(emoticons)
    lu=len(users)

    sale_emoticon_40=[0]*le
    
    for i in range(le):
        sale_emoticon_40[i]=int(emoticons[i]*0.6)
    
    for i in range(lu):
        user=users[i]
        
            







    return answer