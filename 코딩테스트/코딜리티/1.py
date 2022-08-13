

def solution(A):
    current_pointer=0
    bulbs=[False]*(len(A)+1)
    bulbs[0]=True

    ans=0
    for i in A:
        bulbs[i]=True
        flag=False
        for j in range(current_pointer,i):
            if bulbs[j]==False:
                flag=True
                break
        if not flag:
            ans+=1
            current_pointer=i


    print(ans,'asdf')
    return ans




a=[2,3,4,1,5]
b=[1,3,4,2,5]
c=[2,1,3,5,4]
d=[1,2,3,4,5]
e=[5,4,3,1,2]
f=[1,3,4,5,2]
g=[]
h=[2,3,1,4]
i=[x for x in range(100000,0,-1)]
solution(i)