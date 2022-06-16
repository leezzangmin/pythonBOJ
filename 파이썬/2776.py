import sys;input=sys.stdin.readline

def bs(find_list,list_length,number):
    l=0
    r=list_length-1
    
    while l<=r:
        mid=(l+r)//2
       # print(mid,'asdf')
        if find_list[mid]==number:
            return 1
        elif find_list[mid]<number:
            l=mid+1
        else:
            r=mid-1

    return 0




T=int(input())

for _ in range(T):
    S1N=int(input())
    S1=sorted(list(map(int,input().split()))) # 1,2,3,4,5
    S2N=int(input())
    S2=list(map(int,input().split())) # 1,3,5,7,9

    for i in range(S2N):
        print( bs(S1, S1N, S2[i] ) )
    # m={}
    # for i in range(S1N):
    #     m[S1[i]]=1
    # for i in S2:
    #     if i in m:
    #         print(1)
    #     else:
    #         print(0)
