import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**6)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y,ll,maps):
    global N
    global M
    global visit

    ll[ord(maps[x][y])-65]+=1
    visit[x][y]=True
    for i in range(4):
        mx=x+dx[i]
        my=y+dy[i]
        if 0<=mx<N and 0<=my<M and visit[mx][my]==False and maps[mx][my]!='.':
            dfs(mx,my,ll,maps)
    return ll

def solution(maps):
    global visit
    global M
    global N

    answer = 0
    N=len(maps)
    M=len(maps[0])

    global_area=[0]*26

    visit=[[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visit[i][j]==False and maps[i][j]!='.':
                templ=[0]*26
                dfs(i,j,templ,maps)
                mv=max(templ)
                pointer=0
                for k in range(25,-1,-1):
                    if templ[k]==mv:
                        pointer=k
                        break
                gong_nap=0
                if templ.count(mv)!=1:
                    for ii in range(26):
                        if templ[ii]<mv:
                            gong_nap+=templ[ii]
                            templ[ii]=0
                    templ[pointer]+=gong_nap
                else:
                    s=sum(templ)
                    templ=[0]*26
                    templ[pointer]=s
                for mm in range(26):
                    global_area[mm]+=templ[mm]

    #max
    #print(global_area,'global')
    return max(global_area)
