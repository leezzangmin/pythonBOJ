import sys;input=sys.stdin.readline
N=int(input())
s=sorted( list(map(int,input().split())) )


left = 0
right = N - 1
answer = s[left] + s[right]
al = left
ar = right
while left < right:
    tmp = s[left] + s[right]
    if abs(tmp) < abs(answer):
        answer = tmp
        al = left
        ar = right
        if answer == 0:
            break
    if tmp < 0:
        left += 1
    else:
        right -= 1
print(s[al], s[ar])