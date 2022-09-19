def diff(a,b):
    temp=0
    for p in range(len(a)):
        if a[p]!=b[p]:
            temp+=1
    if temp==1:
        return True
    return False

def dfs(cur, level, t, words):
    global visit
    for i in range(len(words)):
        if diff(cur,words[i]) and visit[i]>level+1:
            visit[i]=level+1
            dfs(words[i], level+1, t, words)

            
def solution(begin, target, words):
    global visit
    answer = 0
    visit = [10**8] * len(words)
    if target not in words:
        return 0
    
    dfs(begin, 0, target, words)
    asdf=words.index(target)
    
    return visit[asdf]
