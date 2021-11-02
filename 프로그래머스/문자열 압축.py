import sys


def solution(s):
    ans=sys.maxsize
    l=len(s)
    
    for i in range(2,3):#l//2+1):
        count=0
        for j in range(l):
            print(s[j:j+i],j)
            print(s[j+i:j+i+i])
            #if s[j:j+i]==s[j+i:j+i+i]








if __name__=="__main__":
    a="aabbaccc"
    b="ababcdcdababcdcd"
    c="abcabcdede"	
    d="abcabcabcabcdededededede"	
    e="xababcdcdababcdcd"	
    solution(a)