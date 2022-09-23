N=list(input())
N.sort(reverse=True)

s=0
for i in N:
    i=int(i)
    s+=i
if N[-1] != '0' or s%3!=0:
    print(-1)
else:
    print("".join(N))



# 99999467125413451250
