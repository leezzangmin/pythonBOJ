import math
N=input()
n=[0] * 10
sixnine=0
pointer=len(N)-1

while pointer!=-1:
    if int(N[pointer])==6 or int(N[pointer])==9:
        sixnine+=1
    else:
        n[int(N[pointer])]+=1
    pointer-=1
nM=max(n)
sixnine=math.ceil(sixnine/2)

print(max(sixnine,nM))

