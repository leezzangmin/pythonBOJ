import sys;input=sys.stdin.readline
N=int(input())
s=input().rstrip()
num=[0]*26
for i in range(len(s)):
    if 91>ord(s[i])>64 and num[ord(s[i])-65] == 0:
        num[ord(s[i])-65]=int(input())
#print(num)


stack=[]
ans=0
for i in range(len(s)):
    if (91>ord(s[i])>64):
        stack.append(s[i])
    else:
        a=stack.pop()
        b=stack.pop()
        try:
            a=num[ord(a)-65]
        except:
            pass
        try:
            b=num[ord(b)-65]
        except:
            pass
        stack.append( eval(   str(b) + s[i] + str(a)    )    )

print('%.2f' %float(stack[0]))