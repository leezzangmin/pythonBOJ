import sys;input=sys.stdin.readline;import math;from collections import Counter
N=int(input())
numbers=[0]*N
d={}
for i in range(N):
    numbers[i]=int(input())
def common(numbers):
    c=Counter(numbers)
    cc=c.most_common()
    cc.reverse()
    temp=cc.pop()
    while cc:
        temp2=cc.pop()
        if temp2[1]==temp[1]:
            return temp2[0]
        else:
            return temp[0]

    return temp[0]


numbers.sort()
s1=round(sum(numbers)/N)
print(s1)
s2=numbers[int((N-1)/2)]
print(s2)
s3=common(numbers)
print(s3)
s4=numbers[-1]-numbers[0]
print(s4)



