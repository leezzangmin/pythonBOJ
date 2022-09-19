from collections import deque
Q=deque()
Q.append((1,2))

for x,y in Q:
    print(x,y)
#print(Q.popleft())
print(len(Q))
