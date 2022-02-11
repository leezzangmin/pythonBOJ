# 1 ≤ N ≤ 10**9,
# 1 ≤ M ≤ 300,000
# M ≤ N
import sys;input=sys.stdin.readline
N,M=map(int,input().split())
jewel=[0]*M
left=1
right=0
for i in range(M):
    jewel[i]=int(input())
    right=max(jewel[i],right)


while left <= right:
    mid = (left+right) // 2
    total = 0
    for color in jewel:
        if color % mid == 0:
            total += color//mid
        else:
            total += (color//mid) + 1

    if total > N:
        left = mid + 1

    else:
        right = mid - 1

print(left)