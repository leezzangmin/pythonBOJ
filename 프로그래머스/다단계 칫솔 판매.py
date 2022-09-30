from collections import defaultdict
import math
import sys
sys.setrecursionlimit(10**6)
def dfs(x,money):
    global graph
    global answer
    #print(money,'mmm')
    mm=int(money*0.1)
    answer[x]+=money-mm
    for mx in graph[x]:
        dfs(mx,mm)



def name_to_index(name):
    global name_dict
    return name_dict[name]
def solution(enroll, referral, seller, amount):
    global name_dict
    global graph
    global answer
    le=len(enroll)
    answer=[0 for _ in range(le+1)]

    name_dict=defaultdict(int)
    name_dict["-"]=0
    for i in range(1,le+1):
        name_dict[enroll[i-1]]=i

    graph=[ [] for _ in range(le+1) ]
    for i in range(le):
        graph[i+1].append(name_to_index(referral[i]))
    ls=len(seller)
    for i in range(ls):
        dfs(name_to_index(seller[i]),amount[i]*100)
       # print(answer)

    
    return answer[1:]

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
["young", "john", "tod", "emily", "mary"],
[12, 4, 2, 5, 10]),'answer')

#print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["123", "123", "mary", "edward", "mary", "mary", "jaimie", "edward"],["sam", "emily", "jaimie", "edward"],[2,3,5,4]))