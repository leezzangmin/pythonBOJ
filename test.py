import bisect

l=[-3,-2,1,0,1,2,3,4,100,200,300,400]

a=bisect.bisect_left(l,-3)
b=bisect.bisect_right(l,-3)
print(a)
print(b)