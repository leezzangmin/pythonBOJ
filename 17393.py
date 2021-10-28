# 현재 위치보다 오른쪽에 있으면서 점도지수 Bi 가 서 있는 칸의 잉크지수 Ai 이하인 칸을 칠할 수 있다.
import sys;input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))




for i in range(N):
    start=i
    end=N-1
    while start<=end:
        mid=(start+end)//2
        if B[mid] <= A[i]:
            temp=mid
            start=mid+1
        else:
            end=mid-1
    print(temp-i,end=' ')
print()
