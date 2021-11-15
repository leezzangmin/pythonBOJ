import math
D,H,W=map(int,input().split())


H2=H*H
W2=W*W
D2=D*D

a=math.sqrt(D2/(H2+W2))

print(math.floor(a*H),math.floor(a*W))
#print(math.floor(a*H))