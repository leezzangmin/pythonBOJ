N=input()
numbers=[0 for x in range(0,10)]
for i in N:
    numbers[int(i)]+=1

for i in range(9,-1,-1):
    for _ in range(numbers[i]):
        print(i,end='')