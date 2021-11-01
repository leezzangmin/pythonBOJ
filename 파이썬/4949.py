import sys;input=sys.stdin.readline
s=input().rstrip()
while s!='.':
    stack=[]
    ans='yes'
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(s[i])
        elif s[i]=='[':
            stack.append(s[i])

        elif s[i]==')':
            if stack:
                if stack.pop()=='(':
                    continue
                else:
                    ans='no'
                    break
            else:
                ans='no'
                break
        elif s[i]==']':
            if stack:
                if stack.pop()=='[':
                    continue
                else:
                    ans='no'
                    break
            else:
                ans='no'
                break


        else:
            continue



    if stack:
        print('no')
    else:
        print(ans)
    s=input().rstrip()
