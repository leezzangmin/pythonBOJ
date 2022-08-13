# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# U랑 W 사이에 있으면 엄격하게 누워있다고 표현?
# 비어있지 않은 N개의 정수로 이루어진 배열을 줌
# (P,Q)로 된 쌍을 줌 0<=P<Q<N
# 배열의 어떤 값도 값 a[P]와 a[Q] 사이에 엄격하게 위치하지 않으면 한 쌍의 인덱스가 인접한 값을 갖는다고 합니다. 
# a[P]가 4고 a[Q]가 6인데 배열에 5가 없으면 성립하는듯
# a[1]이 3이고 a[2]가 3이면 둘사이에 값 없으니까 성립 -> dist = 0

# 거리는 abs(A[P]-A[Q]) -> dist(A[4],A[5]) = abs(5-3) =2
# 최소거리가 100,000,000보다 크면 -1 리턴
# 아무 쌍도 없으면 -2 리턴

# 1<=N<=40000
# 각 원소는 -21억 ~ +21억

# import random;a=[random.randint(-2147483648,2147483647) for i in range(40000)]
# a배열 효율성 테스트 통과 못할듯

import copy

def binary(arr,target):
    N=len(arr)
    start=0
    end=N-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
            
        elif arr[mid] > target:
            end=mid-1
        else:
            start=mid+1
def solution(A):
    N=len(A)
    copy_a=sorted(copy.deepcopy(A))
    ans=922337203685477580700

    for i in range(N):
        for j in range(i+1,N):
            if A[i]==A[j]:
                return 0
            else:
                if abs(A[i]-A[j])<ans:
                    if A[i]>A[j]:
                        s,e=A[j],A[i]
                    else:
                        s,e=A[i],A[j]
                    left=binary(copy_a,s)
                    right=binary(copy_a,e)
                    if left+1 != right: # 사이에 값이 있음
                        continue
                    else: #사이에 값 없음
                        ans=min(ans,abs(A[i]-A[j]))

    if ans==922337203685477580700:
        return -2
    elif ans>100000000:
        return -1
    return ans


# def solution2(A):
#     N=len(A)
#     copy_a=sorted(copy.deepcopy(A))
#     Q=deque()
#     ans=100000001

#     for i in range(N):
#         for j in range(i+1,N):
#             if A[i]==A[j]:
#                 Q.append((i,j))
#                 return 0
#             else:
#                 if abs(A[i]-A[j])<ans:
#                     if A[i]>A[j]:
#                         s=A[j]
#                         e=A[i]
#                     else:
#                         s=A[i]
#                         e=A[j]
#                     flag=False
#                     for k in range(s+1,e):
#                         if flag:
#                             break
#                         start=0
#                         end=N-1
#                         while start<=end:
#                             mid=(start+end)//2
#                             if copy_a[mid]==k:
#                                 flag=True
#                                 break
#                             elif copy_a[mid] > k:
#                                 end=mid-1
#                             else:
#                                 start=mid+1
#                     if not flag:
#                         Q.append((i,j))

#     # print(Q,'asdf')
#     if len(Q)==0:
#         return -2
#     while Q:
#         a,b=Q.popleft()
#         ans=min(ans,abs(A[a]-A[b]))
#     if ans>100000000:
#         return -1
#     return ans
    


a=[4,2,1]

print(solution(a))

# p= [ (0, 7),   (1, 2),   (1, 4),
#   (1, 5),   (1, 7),   (2, 4),
#   (2, 5),   (2, 7),   (3, 4),
#   (3, 6),   (4, 5),   (5, 7)]