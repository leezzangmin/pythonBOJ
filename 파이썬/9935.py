
s=input()
bomb=input()
bombl=list(bomb)
ls=len(s)
lb=len(bomb)
last_word=bomb[-1]
stack=[]
for i in range(ls):
    stack.append(s[i])
    if s[i]==last_word:
        lst=len(stack)
        if lst>=lb:
            if stack[lst-lb:]==bombl:
                for _ in range(lb):
                    stack.pop()
        else:
            continue


                
ans="".join(stack)
if len(ans)==0:
    print("FRULA")
else:
    print(ans)

# C1CCCC11C111
# C11