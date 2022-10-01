# 모든 달은 28일까지 있음
from collections import defaultdict


def solution(today, terms, privacies):
    answer = []
    today=today.split(".")
    today_year=int(today[0])
    today_month=int(today[1])
    today_day=int(today[2])

    term_dict=defaultdict(int)
    for t in terms:
        t=t.split(" ")
        term_dict[t[0]]=int(t[1])
   # print(term_dict,'dict')

    lp=len(privacies)
    for i in range(lp):
        p=privacies[i].split(" ")
        date=p[0].split(".")
        target_year=int(date[0])
        target_month=int(date[1])
        target_day=int(date[2])
        

        validate_duration_month = term_dict[p[1]]

        plus_year=validate_duration_month // 12
        plus_month=validate_duration_month % 12

        target_year+=plus_year
        target_month+=plus_month
        target_day-=1

        if target_day==0:
            target_day=28
            target_month-=1
        if target_month==0:
            target_year-=1
            target_month=12

        if target_month>12:
            target_year+=1
            target_month-=12
    
        print(target_year,target_month,target_day,'generated date',date)
        
        if target_year > today_year:
            continue
        elif target_year < today_year:
            answer.append((i+1))
            continue

        # year이 같으면
        if target_month > today_month:
            continue
        elif target_month < today_month:
            answer.append((i+1))            
            continue
        
        # month가 같으면
        if target_day > today_day:
            continue
        elif target_day < today_day:
            answer.append((i+1))
            continue

    #print(today)
    return answer # 파기해야할 친구들 return

#print(solution("2022.01.01", ['A 24', 'B 12', 'C 12'], ['2021.01.02 A', '2021.01.01 B', '2022.02.19 C', '2022.02.20 C']))
print(solution("2020.01.01", ['Z 3', 'D 12'], ['2019.01.01 D', '2019.11.15 Z', '2019.08.02 D', '2019.07.01 D', '2018.12.28 Z']))


# 2020년1월1일에 12개월 동의 --> 2021/01/0 -->  2020년 12월28일
# MM이랑 DD int로 변환했다가 str로 다시 변환할 때 0붙이기
# answer 배열에 +1씩 해서 넣어야함
# 유효기간 = 1이상 100이하