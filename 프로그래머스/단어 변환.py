def diff(a,b):
    temp=0
    for p in range(len(a)):
        if a[p]!=b[p]:
            temp+=1
    if temp==1:
        return True
    return False

def dfs(cur, level, t,words):
    print(cur,'asdf',level,t)
    global visit
    if cur == t:
        print('aszmfioszjf',level)
        return level
    for i in range(len(words)):
        if diff(cur,words[i]) and visit[i]==False:
            visit[i]=True
            dfs(words[i], level+1, t, words)
            
def solution(begin, target, words):
    global visit
    answer = 0
    visit = [False] * len(words)
    if target not in words:
        return 0
    answer = dfs(begin, 0, target, words)
    print('answer',answer)
    return answer

solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])