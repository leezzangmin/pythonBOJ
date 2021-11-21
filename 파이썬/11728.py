import sys;input=sys.stdin.readline
Size_Of_A,Size_Of_B=map(int,input().split())
A=sorted(list(map(int,input().split())))
B=sorted(list(map(int,input().split())))

C=sorted(A+B)
for i in C:
    print(i,end=' ')
print()



# https://jokerldg.github.io/algorithm/2021/08/03/array-combine.html

# 투포인터 풀이
# import sys

# read = lambda: sys.stdin.readline().rstrip()

# N, M = map(int, read().split())

# A = list(map(int, read().split()))
# B = list(map(int, read().split()))
# answer = []

# a_pointer, b_pointer = 0, 0
# a_length, b_length = len(A), len(B)

# while a_pointer != a_length or b_pointer != b_length:
#     if a_pointer == a_length:
#         answer.append(B[b_pointer])
#         b_pointer += 1
#     elif b_pointer == b_length:
#         answer.append(A[a_pointer])
#         a_pointer += 1
#     else:
#         if A[a_pointer] < B[b_pointer]:
#             answer.append(A[a_pointer])
#             a_pointer += 1
#         else:
#             answer.append(B[b_pointer])
#             b_pointer += 1

# print(*answer)