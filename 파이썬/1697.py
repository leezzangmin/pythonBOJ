from collections import deque
N,K=map(int,input().split())
end=100000
s=[0]*(end+1)

# if N>K:
#     s=[0]*(N+1)
#     end=N
# else:
#     s=[0]*(K+1)
#     end=K

Q=deque()
Q.append((N,0))
while Q:
    cur,time=Q.popleft()
    a,b,c=cur-1,cur+1,cur*2
    time+=1
    if 0<=a<=end and s[a]==0:
        s[a]=time
        Q.append((a,time))
    if 0<=b<=end and s[b]==0:
        s[b]=time
        Q.append((b,time))
    if 0<=c<=end and s[c]==0:
        s[c]=time
        Q.append((c,time))

if N==K:
    print(0)
else:
    print(s[K])
