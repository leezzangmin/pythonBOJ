import sys;input=sys.stdin.readline
STRING=[0]*600000
s=input().rstrip()
for i in range(len(s)):
    STRING[i]=[s[i],i-1,i+1]
STRING[0][1]=False
STRING[len(s)-1][2]=False

# ['a', False, 1], ['b', 0, 2], ['c', 1, 3], ['d', 2, False],
M=int(input())
pointer=len(s)
for _ in range(M):
    o=input().split()

    if o[0]=='L':
        if STRING[pointer-1][1]:
            pointer=STRING[pointer-1][1]
    elif o[0]=='D':
        if STRING[pointer-1][2]:
            pointer=STRING[pointer-1][1]
    elif o[0]=='B':

    else:



# for i in s:
#     print(i,end='')


# dmih
# dmi
# dm
# dmx
# dm'x
# d'x
# 'x
# 'yx
# yx'
# yx'z
