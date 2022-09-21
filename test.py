from collections import defaultdict
d=defaultdict()
try:
    d[(3,3)].append([2,2])
except:
    d[(3,3)]=[[2,2]]

try:
    d[(3,3)].append([100,2])
except:
    d[(3,3)]=[2,2]


try:
    d[(3,3)].append([9999,2])
except:
    d[(3,3)]=[2,2]


print(d[3,3])
print(d[1,1])