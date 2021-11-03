# import sys


# def solution(s):
#     answer=sys.maxsize
#     l=len(s)
    
#     for i in range(1,l//2+1):
#         temp1=""
#         print(i,'i')
#         count=1
#         temp2=s[0:i]
#         for j in range(i,l,i):
#             if temp2==s[j:j+i]:
#                 count+=1
#             else:
#                 if count==1:
#                     temp1+=temp2
#                 else:
#                     temp1+=str(count)+temp2
#                     temp2=s[j:j+i]
#                     count=1
        
        
#         print(temp1,'temp')
#         answer=min(len(temp1),answer)
#     return answer






# if __name__=="__main__":
#     a="aabbaccc"
#     b="ababcdcdababcdcd"
#     c="abcabcdede"	
#     d="abcabcabcabcdededededede"	
#     e="xababcdcdababcdcd"	
#     print(solution(a))
    