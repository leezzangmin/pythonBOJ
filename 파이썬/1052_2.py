N,K=map(int,input().split())

if N<=K:
    print(0)
    exit()
for i in range(1,987654321):
    if bin(N+i)[2:].count('1')<=K:
        print(i)
        exit()