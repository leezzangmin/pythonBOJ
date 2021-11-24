import sys;from collections import deque
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    f=True
    direction=True # True: 왼쪽에서 제거 , False: 오른쪽에서 제거
    p=input().rstrip()
    n=int(input())
    x=deque()
    temp=input().rstrip().replace('[',"").replace(']',"").split(',')
    for i in temp:
        if i=='':
            continue
        x.append(int(i))


    for i in p:
        if i=='R':
            direction = (not direction)

        else:
            try:
                x[0]
                if direction:
                    x.popleft()
                else:
                    x.pop()
            except:
                print('error')
                f=False
                break
    if f:
        if direction:
            print(str(list(x)).replace(' ',''))
        else:
            print(str(list(x)[::-1]).replace(' ',''))
[2, 1]
[2,1]