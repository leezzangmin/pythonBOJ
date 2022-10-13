N=int(input())
words=['']*N
for i in range(N):
    words[i]=input()

lw=len(words[0])
answer=''
for i in range(lw):
    flag=False
    c=words[0][i]
    for j in words:
        if j[i]!=c:
            flag=True
           # break
   # print(i,'ii')
    if flag:
        answer+='?'
    else:
        answer+=c
print(answer)

