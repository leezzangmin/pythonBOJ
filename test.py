from itertools import combinations
from collections import deque
a=[(1,2),(2,3),(3,4),(4,5)]
c=combinations(a,2)
for i in c:
    print(list(i))
    print(deque(i))