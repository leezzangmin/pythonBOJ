import sys;input=sys.stdin.readline



if __name__=="__main__":
    n=int(input())
    s=list(map(int,input().split()))
    x=int(input())

    s.sort()
  #  print(s)
    start,end=0,n-1
    ans=0
    while start<end:
        print(start,end)
        a=s[start]+s[end]
        if a==x:
            ans+=1
        if a<x:
            start+=1
            continue
        end-=1


    print(ans)