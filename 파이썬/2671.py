
# import re
# s=input()
# r=re.compile('(100+1+|01)+')
# if r.fullmatch(s):
#     print("SUBMARINE")
# else:
#     print("NOISE")

import sys;
s=input()
nn="NOISE"
ss="SUBMARINE"

try:
    while len(s)!=0:
        print(s,'ss')
        if s[0:2]=='10':
            s=s[2:]
            i=0
            while s[i]=='0':
                i+=1
            s=s[i:]
            i=0
        #  print(s,'asdf')
            while i!=len(s) and s[i]=='1':
                i+=1
            s=s[i:]
        if len(s)!=0 and s[0]=='0':
            if s[1]=='1':
                s=s[2:]
            else:
                s=s[1:]
        print(s,'ss')
        if s[0:2]=='11':
            raise Exception()
except:
    print(nn)
    sys.exit()
    

print(ss)
