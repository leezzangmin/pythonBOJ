import sys;input=sys.stdin.readline
N=int(input())
s=list(input().rstrip() for _ in range(N))

def isGood(S):
    if len(S)%2==1:
        return False
    L=[]
    for i in range(len(S)):
        if L:
            if L[-1]==S[i]:
                L.pop()
            else:
                L.append(S[i])
        else:

            L.append(S[i])
             

    if L:
        return False
    else:
        return True




    
ans=0
for i in range(N):
    if isGood(s[i]):
        ans+=1
print(ans)
