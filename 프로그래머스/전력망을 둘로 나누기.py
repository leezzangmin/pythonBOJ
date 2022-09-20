def dfs(start,graph,count,visit):
    visit[start]=True

    for node in graph[start]:
        if visit[node]==False:
            visit[node]=True
            count=max(count,dfs(node,graph,count+1,visit))

    return count

        
def solution(n, wires):
    answer = int(1e9)
    lw=len(wires)
        
    for i in range(lw):        
        graph=[[] for _ in range(n+1)]
        for k in range(lw):
          #  print(k,'kkk')
            if k!=i:
                x,y=wires[k][0],wires[k][1]
                graph[x].append(y)
                graph[y].append(x)
        
        counts=[]
        visit=[False]*(n+1)
        #print(graph,'graph')
        for j in range(1,n+1):
            if visit[j]==False:
                counts.append(dfs(j,graph,1,visit))
       # print(counts,'ㅁㄴㅇㄹ')

        answer=min(abs(counts[1]-counts[0]),answer)
        
    return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4,[[1,2],[2,3],[3,4]]))
print(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))