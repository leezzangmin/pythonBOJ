from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    d=defaultdict(int)
    for t in tangerine:
        d[t]+=1
    ld=len(d)
    s=[0]*ld
    s=sorted(list(d.values()),reverse=True)

    for i in range(ld):
        if k>0:
            k-=s[i]
            answer+=1
        else:
            break
    return answer

print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))