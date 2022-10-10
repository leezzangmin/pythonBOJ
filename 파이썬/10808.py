S=input()
l=[0]*26
for i in S:
    l[ord(i)-97]+=1
for i in l:
    print(i,end=' ')

