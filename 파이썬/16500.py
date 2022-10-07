import sys;input=sys.stdin.readline
s=input().rstrip()
ls=len(s)
dp=[0]*(ls+1)
N=int(input())
words=set()

for i in range(N):
    words.add(input().rstrip())

end=ls
for i in range(ls-1,-1,-1):
    temps=s[i:ls]
    print(temps,'tempS')
    for w in words:
        if temps.startswith(w):
            dp[i]=1
            break

    #if temps in words:
    #    dp[i]=1
    #    end=i
print(dp)
print(dp[0])
    


#softwarecontest
#000000001000000
#3
#soft 
#software 
#contest