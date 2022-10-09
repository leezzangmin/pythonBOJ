# 플레이어 m명 1단계에 있고 N단계 더 있음
import heapq

def getMinimumHealth(initial_players, new_players, rank):
    answer = 0
    cur_num_of_player=len(initial_players)
    for i in range(cur_num_of_player):
        initial_players[i]=initial_players[i]*-1
    lp=len(new_players)
    for i in range(lp):
        new_players[i]=new_players[i]*-1
    
    heapq.heapify(initial_players)

    rank_list=[0]*rank
    for i in range(rank):
        rank_list[i]=heapq.heappop(initial_players)
    answer+=rank_list[-1]
    for i in range(rank):
        heapq.heappush(initial_players,rank_list[i])

    for i in range(lp):
        heapq.heappush(initial_players,new_players[i])
        for j in range(rank):
            rank_list[j]=heapq.heappop(initial_players)
        answer+=rank_list[-1]
        for j in range(rank):
            heapq.heappush(initial_players,rank_list[j])
    
    return abs(answer)
