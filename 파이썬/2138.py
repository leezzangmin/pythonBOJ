#https://velog.io/@jkh9615/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-2138-%EC%A0%84%EA%B5%AC%EC%99%80-%EC%8A%A4%EC%9C%84%EC%B9%98-Java
# https://velog.io/@dding_ji/baekjoon2138
# 그리디 어려워ㅠㅠ
from sys import stdin
import copy

N = int(stdin.readline())
A = list(map(int, stdin.readline().rstrip()))
B = list(map(int, stdin.readline().rstrip()))

r1 = copy.deepcopy(A)
r2 = copy.deepcopy(A)


def two_flip(i, j):
    A[i] = 1 - A[i]
    A[j] = 1 - A[j]

def three_flip(i, j, k):
    A[i] = 1 - A[i]
    A[j] = 1 - A[j]
    A[k] = 1 - A[k]

for i in range(2):
    A = r1 if i == 0 else r2
    cnt = 0
    for j in range(N):
        if j == 0:
            if i == 0 and A != B:
                cnt += 1
                two_flip(j, j+1)

        elif 1 <= j <= N-2:
            if A[j-1] != B[j-1]:
                cnt += 1
                three_flip(j-1, j, j+1)

        elif j == N-1:
            if A[j-1] != B[j-1]:
                cnt += 1
                two_flip(j-1, j)

    if A == B:
        print(cnt)
        break

if A != B:
    print(-1)