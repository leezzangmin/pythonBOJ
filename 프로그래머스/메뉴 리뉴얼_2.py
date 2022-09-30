from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    answer = []
    menu=defaultdict(int)
    for c in course:
        for o in orders:
            o="".join(sorted(o))
            for combo in combinations(o,c):
                menu[combo]+=1
   # for i in menu:
   #     print(i)
  #  print(menu)
    for c in course:
        mv=-1
        for i in menu:
            if len(i)==c:
                mv=max(mv,menu[i])
        if mv>1:
            for i in menu:
                if len(i)==c and menu[i]==mv:
                    answer.append("".join(i))
    answer.sort()

    
    



    return answer

#print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
solution(	["XYZ", "XWY", "WXA"],[2,3,4])