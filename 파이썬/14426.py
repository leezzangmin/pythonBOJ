import sys;input=sys.stdin.readline
from collections import defaultdict
N,M=map(int,input().split())
d=defaultdict()

def insert(D,string,length):
    if length!=0:        
        if string[0] not in D:
            D[string[0]]=defaultdict()
        insert(D[string[0]],string[1:],length-1)
    
#            D[string[i]]=defaultdict()
def search(DD,string,length):
   # print(DD,string,'string')
    r=True
    if length!=0:
        if string[0] in DD:
            r=search(DD[string[0]],string[1:],length-1)
        else:
            r=False
    return r

for i in range(N):
    s=input().rstrip()
    insert(d,s,len(s))

ans=0
for i in range(M):
    s=input().rstrip()
    ls=len(s)    
    if ls>0 and search(d,s,ls):
        ans+=1
print(ans)

#print(d)
