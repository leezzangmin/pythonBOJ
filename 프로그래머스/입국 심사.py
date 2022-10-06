import sys
def solution(n, times):
    answer = 0
    times.sort()
    l=1;r=sys.maxsize
    
    while l<=r:
        mid=(l+r)//2
        temp=0
        for t in times:
            temp+=mid//t
            if temp>n:
                break
        
        if temp>=n:
            answer=mid
            r=mid-1
            
        else:
            l=mid+1
 
    return answer