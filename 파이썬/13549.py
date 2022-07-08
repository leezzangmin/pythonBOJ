import sys;input=sys.stdin.readline

subin,dongsaeng=map(int,input().split())
asdf=[99]*200001
asdf[0]=0
asdf[subin]=0


def move(cur):
    asdf[cur]=min(asdf[cur+1]+1,asdf[cur-1]+1,asdf[cur])
    asdf[cur-1]=min(asdf[cur-1],asdf[cur]+1)
    asdf[cur+1]=min(asdf[cur+1],asdf[cur]+1)
    asdf[cur*2]=min(asdf[cur*2],asdf[cur])




for i in range(1,100001):
    move(i)

print(asdf[dongsaeng])