N=int(input())
s=[0]*N
for i in range(N):
    s[i]=int(input())
s.sort()
for i in range(N):
    print(s[i])