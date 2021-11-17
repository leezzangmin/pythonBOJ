import sys
from collections import defaultdict

sys.setrecursionlimit(int(1e4))
n = int(sys.stdin.readline().rstrip())
tree = defaultdict(list)
answer = 0

for _ in range(n-1):
    a, b, w = map(int, sys.stdin.readline().rsplit())
    tree[a].append((b, w))

def solve(node, cost):
    if not tree[node]: return cost
    total = 0
    m = 0
    for next_node, w in tree[node]:
        m = solve(next_node, cost+w)
        if total < m: total = m
    
    return total

for node in range(n):
    tmp = []
    for next_node, w in tree[node]:
        tmp.append(solve(next_node, w))
    
    tmp.sort(reverse=True)
    total = sum(tmp[:2])
    if answer < total: answer = total

print(answer)