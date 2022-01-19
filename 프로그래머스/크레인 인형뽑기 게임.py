def solution(board, moves):
    bagooni=[-999]
    length=len(board)
    answer = 0

    for move in moves:
        move-=1
        for x in range(length):
            if board[x][move]!=0:
                if bagooni[-1]==board[x][move]:
                    bagooni.pop()
                    answer+=2
                else:
                    bagooni.append(board[x][move])
                board[x][move]=0
                print(bagooni)
                break

    


    # for i in board:
    #     print(i)
    # print(bagooni)
    # print(answer)
    return answer


board=[ [0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]	
print(solution(board,moves))


