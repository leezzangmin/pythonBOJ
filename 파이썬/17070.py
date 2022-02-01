# import sys;input=sys.stdin.readline
# from collections import deque
# dx=[0,1]
# dy=[1,0]
# ds=[0,1]
# N=int(input())
# house=list(list(map(int,input().split())) for _ in range(N))
# Q=deque()
# Q.append((0,1,0))
# M=N-1
# ans=0
# def bfs():
#     global ans
#     while Q:
#         x,y,s=Q.popleft()
#         if x==M and y==M:
#             ans+=1
#             continue
#         if s==0:
#             mx=x
#             my=y+1
#             if 0<=my<N and house[mx][my]!=1:
#                 Q.append((mx,my,0))
#                 if 0<=x+1<N and house[x+1][y]!=1 and house[x+1][my]!=1:
#                     Q.append((x+1,my,2))
#         elif s==1:
#             mx=x+1
#             my=y
#             if 0<=mx<N and house[mx][my]!=1:
#                 Q.append((mx,my,1))
#                 if 0<=y+1<N and house[x][y+1]!=1 and house[mx][y+1]!=1:
#                     Q.append((mx,y+1,2))
#         else:
#             mx=x
#             my=y+1
#             if 0<=my<N and house[mx][my]!=1:
#                 Q.append((mx,my,0))
#             mx=x+1
#             my=y
#             if 0<=mx<N and house[mx][my]!=1:
#                 Q.append((mx,my,1))
#                 if 0<=y+1<N and house[x][y+1]!=1 and house[mx][y+1]!=1:
#                     Q.append((mx,y+1,2))
# bfs()
# print(ans)
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 0: 가로로 온 수 / 1: 세로로 온 수 / 2: 대각선으로 온 수
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1
i = 2
while i < n:
    if arr[0][i]:
        break
    dp[0][0][i] = 1
    i += 1

for i in range(1, n):
    for j in range(2, n):
        if arr[i][j] == 0 and arr[i][j - 1] == 0 and arr[i - 1][j] == 0:
            dp[2][i][j] = sum(dp[k][i - 1][j - 1] for k in range(3))
        if arr[i][j] == 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

print(sum(dp[i][-1][-1] for i in range(3)))