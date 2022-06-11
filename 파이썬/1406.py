import sys;input=sys.stdin.readline

stk1 = list(input().strip())
stk2 = []
n = int(input())
for _ in range(n):
    line=input().split()
    if line[0] == 'L':
        if stk1:
            stk2.append(stk1.pop())
    elif line[0] == 'D':
        if stk2:
            stk1.append(stk2.pop())
    elif line[0] == 'B':
        if stk1:
            stk1.pop()
    else:
        stk1.append(line[1])
print(''.join(stk1 + list(reversed(stk2))))

#이중 연결리스트는 stack 2개로 구현 가능하다 메모...