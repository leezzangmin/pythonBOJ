def dfs(n,ii,length,t):
    a=0
    if ii!=length:
        if ii==length-1 and sum(n)==t:
            a+=1
        a+=dfs(n,ii+1,length,t)

        n[ii]=-n[ii]
        if ii==length-1 and sum(n)==t:
            a+=1
        a+=dfs(n,ii+1,length,t)
    return a

def solution(numbers, target):
    answer = 0
    l=len(numbers)
    answer=dfs(numbers,0,l,target)
    return answer