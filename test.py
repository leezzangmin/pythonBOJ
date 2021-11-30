M,N,H=map(int,input().split())
tomato=[]
for _ in range(H):
    temp=[]
    for i in range(N):
        temp.append(list(map(int,input().split())))
    tomato.append(temp)

print(tomato)
