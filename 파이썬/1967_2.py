# import sys;input=sys.stdin.readline
# from collections import deque
# import heapq
# N=int(input())
# graph=[[] for _ in range(N+1)]
# for i in range(N-1):
#     a,b,cost=map(int,input().split())
#     graph[a].append([b,cost])

# def bfs(x1):
#     return_cost=[]
#     Q=deque()
#     Q.append((x1,0))
#     while Q:
#         x,temp_cost=Q.popleft()
#         print(x,'xxx')
#         for mx,val in graph[x]:
#             print(mx,'mxmx',temp_cost+val)
#             if not graph[mx]:
#                 heapq.heappush(return_cost,-(temp_cost+val))
#             else:
#                 Q.append((mx,temp_cost+val))
#     print(return_cost,'return_cost')
#     print(heapq.heappop(return_cost),heapq.heappop(return_cost),'x1x1')
#     return 1#abs(heapq.heappop(return_cost))+abs(heapq.heappop(return_cost))

# ans=-sys.maxsize
# bfs(1)
# # for i in range(1,N+1):
# #     if graph[i]:
# #         print(i,'index')
# #         print(bfs(i),i,'ii')
# #         #ans=max(ans,bfs(i))
