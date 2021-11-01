from collections import deque
N=int(input())

s=deque([x for x in range(1,N+1)])

while len(s)!=1:
    s.popleft()
    s.append(s.popleft())
print(s[0])