import copy
N=int(input())
before=list(map(int,input()))
after=list(map(int,input()))

def click(x):
    if before[x-1]==1:
        before[x-1]=0
    else:
        before[x-1]=1

    if before[x]==1:
        before[x]=0
    else:
        before[x]=1

    if x+1!=N and before[x+1]==1:
        before[x+1]=0
    elif x+1!=N and before[x+1]==0:
        before[x+1]=1

def click2(x):
    if before1[x-1]==1:
        before1[x-1]=0
    else:
        before1[x-1]=1
    if before1[x]==1:
        before1[x]=0
    else:
        before1[x]=1
    if x+1!=N and before1[x+1]==1:
        before1[x+1]=0
    elif x+1!=N and before1[x+1]==0:
        before1[x+1]=1

before1=copy.deepcopy(before)
if before1[0]==1:
    before1[0]=0
else:
    before1[0]=1
if before1[1]==1:
    before1[1]=0
else:
    before1[1]=1

temp=0
for i in range(1,N):
    if before[i-1]==after[i-1]:
        continue
    click(i)
    temp+=1
if before==after:
    exit()

temp=1
for i in range(1,N):
    if before1[i-1]==after[i-1]:
        continue
    click2(i)
    temp+=1
if before1==after:
    print(temp)
    exit()

print(-1)
