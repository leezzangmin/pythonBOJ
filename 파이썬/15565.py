import sys;
input=sys.stdin.readline
N,K=map(int,input().split())
doll=list(map(int,input().split()))

lion=[]
for i in range(N):
    if doll[i]==1:
        lion.append(i)
if len(lion)<K:
    print(-1)
    sys.exit()
    
L,R=0,K-1
ans=sys.maxsize
while True:
    try: 
        ans=min(ans,lion[R]-lion[L]+1)
    except:
        break
    L+=1
    R+=1
print(ans)