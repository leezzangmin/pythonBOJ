import math
N,K=map(int,input().split())
print(N,K)

currentCapacity=1
restBottle=[]

while N>K:
    print(N,currentCapacity)
    if N%2==1:
        print(N,'asdf')
        restBottle.append(currentCapacity)
    N = math.floor(N/2)
    currentCapacity*=2

print(restBottle,currentCapacity)
answer=0
pointer=0
while True:
    if restBottle[pointer]==currentCapacity:
        break
    elif pointer==len(restBottle)-1:
        answer+=currentCapacity-restBottle[pointer]
        break
    answer+=restBottle[pointer+1]-restBottle[pointer]
    restBottle[pointer+1]*=2
    pointer+=1
    print(restBottle,'dddddddddddddd',pointer,answer)


print(answer,'answer')