def solution(n, k, cmd):
    answer = ''
    pointing=k
    board=[True]*n
    z=[]
    for i in range(len(cmd)):
       # print(pointing,cmd[i])
        if cmd[i][0]=="D":
            count=0
            while count!=int(cmd[i][2:]):
                pointing+=1
                if board[pointing]:
                    count+=1

        elif cmd[i][0]=="C":
            board[pointing]=False
            z.append(pointing)
            if pointing==n-1:
                pointing-=1
                while board[pointing]==False:
                    pointing-=1
            else:
                pointing+=1
                while board[pointing]==False:
                    pointing+=1

        elif cmd[i][0]=="U":
            count=0
            while count!=int(cmd[i][2:]):
                pointing-=1
                if board[pointing]:
                    count+=1

        else:
            board[z.pop()]=True


    for i in board:
        if i:
            answer+='O'
        else:
            answer+='X'
    print(answer)
    return answer

a=8
k=2
cmd=["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
solution(a,k,cmd)