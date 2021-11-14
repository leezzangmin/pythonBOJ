import sys;input=sys.stdin.readline


def dfs(arr,price):
    print(arr,';awefjio')
    global ans
    if len(arr)==1:
        return ans
    else:

        for i in range(len(arr)):
            if arr[i]:
                print(arr[i],'a')
                print(arr[i][0],'b')
                ans+=dfs(arr[i],price+arr[i][1])




if __name__=="__main__":
    N=int(input())
    tree=[ [] for _ in range(N) ]
    for _ in range(N-1):
        a,b,c=map(int,input().split())
        tree[a].append([b,c])
    print(tree)
    for i in range(1,N+1):
        if tree[i]:
            ans=0
            dfs(tree[i],0)
            print(ans)
            