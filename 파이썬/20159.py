# brute-force + prefix-sum
N=int(input())
cards=list(map(int,input().split()))

zzak_sum=[0]*(N//2+1)
hol_sum=[0]*(N//2+1)
for i in range(N):
    ii=i//2+1
    if i%2==0:
        zzak_sum[ii]=zzak_sum[ii-1]+cards[i]
    else:
        hol_sum[ii]=hol_sum[ii-1]+cards[i]

ans=0
for i in range(0,N//2+1):
    # my mit_zzang
    front=zzak_sum[i]
    back=hol_sum[-1]-hol_sum[i]
    ans=max(ans,front+back)

    # his mit_zzang
    front=zzak_sum[i]
    back=hol_sum[-2]-hol_sum[i-1]
    ans=max(ans,front+back)
print(ans)
#print(max(ans,hol_sum[-1]))


# 1 2 3 4 5 6 7 8

# 1 - 2 4 6 ==> 1 3 - 4 6 ==> 1 3 5 - 6
# 3 5 7 - 8
