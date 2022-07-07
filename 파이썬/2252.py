#위상정렬
#학생 A가 학생 B의 앞에 서야 한다는 의미이다.
import sys;input=sys.stdin.readline
from collections import deque
def miller_kakao():
    result=[]
    Q=deque()
    for i in range(1,student_num+1):
        if jinipchasoo[i]==0:
            Q.append(i)
    while Q:
        now=Q.popleft()
        result.append(now)
        for i in graph[now]:
            jinipchasoo[i]-=1

            if jinipchasoo[i]==0:
                Q.append(i)

 
    print(' '.join(map(str,result)))

student_num, compare_num=map(int,input().split())
graph=[[] for _ in range(student_num+1)]
jinipchasoo=[0 for _ in range(student_num+1)]
for _ in range(compare_num):
    A,B=map(int,input().split())
    graph[A].append(B)
    jinipchasoo[B]+=1

miller_kakao()


