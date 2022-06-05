import sys;input=sys.stdin.readline
N=int(input())
books={}
for _ in range(N):
    s=input().rstrip()
    if s in books:
        books[s]+=1
    else:
        books[s]=1
M=-1
for i in books.values():
    M=max(M,i)

anss=[]
for k in books:
    if books[k]==M:
       anss.append(k)
anss.sort()
print(anss[0])
#print(books)
