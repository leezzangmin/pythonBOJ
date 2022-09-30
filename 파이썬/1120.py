A,B=input().split()
la=len(A) #0
lb=len(B) #123
diff=lb-la
ans=int(1e9)
for i in range(diff+1):
    b=B[i:la+i]
    count=0
    for j in range(la):
        if b[j]!=A[j]:
            count+=1
    ans=min(count,ans)
print(ans)
        