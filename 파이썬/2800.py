import itertools

s=input()
stack=[]
combo=[]

ls=len(s)
for i in range(ls):
    if s[i]=='(':
        stack.append(i)
    elif s[i]==')':
        left=stack.pop()
        right=i
        combo.append((left,right))


answer=set()
for i in range(1,len(combo)+1):
    c=itertools.combinations(combo,i)
    for j in c:
        index_set=set()
        for x,y in j:
            index_set.add(x)
            index_set.add(y)
        temp=''
        for k in range(ls):
            if k in index_set:
                continue
            else:
                temp+=s[k]
            
        answer.add(temp)

answer=list(answer)
answer.sort()
for i in answer:
    print(i)