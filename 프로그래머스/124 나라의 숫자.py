# 3진법인것 같음
def solution(n):


    num=[1,2,4]
 
    answer = ''
   
    while n>0:
        n-=1
        a=n%3
        answer+=str(num[a])
        
        n=n//3
  #  print(answer[-1:-len(answer)-1:-1])

    return answer[-1:-len(answer)-1:-1]

#solution(7)
for i in range(1,100):
    solution(i)