from collections import deque
N,K=map(int,input().split())
#N,K=7,3
circle=deque(range(1,N+1))
ans=[]
for i in range(N):
    for j in range(K-1):
        circle.append(circle.popleft())
    ans.append(circle.popleft())


print('<',end='')
for i in range(N-1):
    print(ans[i],end=', ')
print(ans[-1],end='')
print('>')

# result = map(str,ans)
# print('<',end ='')
# print(', '.join(result),end='')
# print('>')
# https://www.acmicpc.net/source/35597794