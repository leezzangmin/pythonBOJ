import sys;input=sys.stdin.readline
from collections import defaultdict

N=int(input())

def insert(D,arr,length):
    if length!=0:
        if arr[0] in D:
            insert(D[arr[0]],arr[1:],length-1)
        else:
            D[arr[0]]=defaultdict()
            insert(D[arr[0]],arr[1:],length-1)
def print_(DD,level):
    for i in sorted(DD):
        # print(i,'iii')
        print(level*dash+i)
        print_(DD[i],level+1)
    
d=defaultdict()
for _ in range(N):
    info=list(input().rstrip().split())
    K=int(info[0])
    insert(d,info[1:],K)
dash='--'
print_(d,0)
