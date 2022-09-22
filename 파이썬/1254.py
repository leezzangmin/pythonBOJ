s=input()
ls=len(s)
stack=[]

#print(s[0:][::-1],'asdf')

if s==s[::-1]:
    print(ls)
    exit()

for i in range(1,ls):
  #  print(s[i:],'1')
   # print(s[-1:i-1:-1],'2')
    if s[i:]==s[-1:i-1:-1]:
        print(ls+i)
        exit()
    #if s[i:]==s[-i::-1]:
    #    print(s,'asdf',i)


    #stack.append(s[i])
# abab : baba
# bab : bab
# ab : ba
# b : b
    

# abba
# abababa