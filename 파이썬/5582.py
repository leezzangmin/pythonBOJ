A=input()
B=input()

arr = [[0]*(len(B)+1) for _ in range(len(A)+1)]
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
            
ans=0
for i in arr:
    ans=max(max(i),ans)
print(ans)