
import sys;input=sys.stdin.readline
N=int(input())


carNumIn={}
for i in range(N):
    carNumIn[input().rstrip()]=i

ans=0
for i in range(N):
    if carNumIn[input().rstrip()]>=i:
        ans+=1


print(ans)


# AA          DD
# BB          AA
# CC          CC
# DD          BB