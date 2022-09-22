import re

T=int(input())

# (100+1+ | 01)+
p=re.compile('(100+1+|01)+')
#print(p,'asdf')
for _ in range(T):
    s=input()
    if re.fullmatch(p,s):
        print("YES")
    else:
        print("NO")
#print(re.fullmatch(p,'10010111'))
#print(re.fullmatch(p,'011000100110001'))
#print(re.fullmatch(p,'0110001011001'))
