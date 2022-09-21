def define_java_c(STRING):
    if len(STRING)==0:
        return 4
    if STRING[0].isupper():
        return 4
    if '_' in STRING:
        ss=STRING.split('_')
        for i in ss:
            if len(i)==0:
                return 4
            else:
                for j in i:
                    if j.isupper():
                        return 4

    for i in STRING:
        if i=='_':
            return True
        elif i.isupper():
            return False
    return 3



s=input()
b=define_java_c(s) # c++
if b==True: # c++
  #  print('c++')
    ss=s.split('_')
    answer=''
    for i in range(len(ss)):
        if i==0:
            answer+=ss[i]
        else:
            temp=len(ss[i])
            if temp==1:
                answer+=ss[i][0].upper()
            else:
                answer+=ss[i][0].upper()+ss[i][1:]
    print(answer)
elif b==False: #java
   # print('java')
    answer=s[0]
    for i in range(1,len(s)):
        if s[i].isupper():
            answer+='_'+s[i].lower()
        else:
            answer+=s[i]
    print(answer)
elif b==3:
    print(s) 
elif b==4:
    print('Error!')
