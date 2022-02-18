import sys;input=sys.stdin.readline
s=input().rstrip()
length=len(s)
answer=[''] * length

space_location=[]

left=0
right=0
while right<length:
    if s[left]=='<':
        while s[right]!='>':
            right+=1
        for i in range(left,right+1):
            answer[i]=s[i]
        
        left=right+1
        right=left
    elif s[right] == ' ':
        j=right-1
        for i in range(left,right):
            answer[i] = s[j]
            j-=1
        answer[right]=" "
        left=right+1
        right=left
    elif s[right] == '<':
        j=right-1
        for i in range(left,right):
            answer[i]=s[j]
            j-=1
        left=right
        right=left
    else:
        right+=1
j=right-1
for i in range(left,right):
    answer[i] = s[j]
    j-=1

print("".join(answer))


# 이게 코드냐