#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
from turtle import distance
#
# Complete the 'minCostPath' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. WEIGHTED_INTEGER_GRAPH g
#  2. INTEGER x
#  3. INTEGER y
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#
#그가 출발한 곳에서 두 개의 심부름 장소를 거쳐 
# 학교까지 가는 가장 빠른 경로를 결정하십시오.
#Jack의 경로는 항상 노드 1에서 시작하고 학교는 항상
# 노드 g_nodes에 있습니다.
# 참고: Jack은 모든 노드를 여러 번 방문할 수 있습니다.

def min(start):
    global distance
    global graph
    h=[]
    heapq.heappush(h,(0,start))
    while h:
        dist,now=heapq.heappop(h)
        if distance[now]<dist:
            continue
        for dest,weight in graph[now]:
            cost=dist+weight
            if distance[dest]>cost:
                distance[dest]=cost
                heapq.heappush(h,(cost,dest))

def minCostPath(g_nodes, g_from, g_to, g_weight, x, y):
    global graph
    # (다익스트라 1에서 x) + (다익스트라 x에서 y) + (다익스트라 y에서 g_nodes)
    answer=sys.maxsize
    
    ln=len(g_from)
    
    graph=list([] for _ in range(ln+1))
    
    for i in range(ln):
        graph[g_from[i]].append((g_to[i],g_weight[i]))
        graph[g_to[i]].append(g_from[i],g_weight[i])

    distance=[sys.maxsize]*(ln+1)
    distance[1]=0
    min(1)
    print(distance[x],'x')
    answer+=distance[x]
    distance=[sys.maxsize]*(ln+1)
    distance[x]=0
    min(x)
    print(distance[y],'y')
    answer+=distance[y]
    distance=[sys.maxsize]*(ln+1)
    distance[y]=0
    min(y)
    print(distance[g_nodes],'gnode')
    answer+=distance[g_nodes]
    return answer