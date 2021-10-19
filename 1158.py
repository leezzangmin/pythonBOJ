from collections import deque
N,K=map(int,input().split())
#N,K=7,3
s=deque(x for x in range(1,N+1))
print(s)

ans=[]
for i in range(N):
    for j in range(K):
        s.append(s.popleft())
    print(s)
    ans.append(s.pop())
    print(ans,'asdf')
print('<',end='')
print(*ans,sep=', ',end='')
print('>')