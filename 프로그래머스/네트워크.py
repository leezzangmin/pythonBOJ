import sys
sys.setrecursionlimit(10**8)

def dfs(computers,i):
    global visit
    visit[i]=True
    for ii in range(len(computers[i])):
        if ii!=i and computers[i][ii]==1 and visit[ii]==False:
            dfs(computers,ii)
            
        

def solution(n, computers):
    global visit
    answer = 0
    l=len(computers)
    visit=[False]*l
    for i in range(l):
        if visit[i]==False:
            dfs(computers,i)
            answer+=1
        
    return answer