from collections import deque
#N,K=map(int,input().split())
N,K=7,3
circle=deque(range(1,N+1))
print(circle)
ans=[]
for i in range(N):
    for j in range(K-1):
        circle.append(circle.popleft())
        print(circle,'2')
    ans.append(circle.popleft())
    print(ans,'asdf')


print('<',end='')
for i in range(N-1):
    print(ans[i],end=', ')
print(ans[-1],end='')
print('>')