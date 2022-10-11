import sys;input=sys.stdin.readline
from collections import defaultdict
N,M=map(int,input().split())
words=defaultdict(int)
for _ in range(N):
    word=input().rstrip()
    lw=len(word)
    if lw>=M:
        count=words[word]
        words[word]=count+1
#print(words)
w=[]
for i in words.keys():
    w.append([words[i],len(i),i])
#print(w,'w')
w.sort(key=lambda x:(-x[0],-x[1],x[2]))

for i in w:
    print(i[2])
#a=list(words.keys)
#print(words.keys)
#words=list(words)
#print(words)
