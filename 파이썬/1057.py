# import sys
# N,K,L=map(int,input().split())


# t=[x for x in range(1,N+1)]

# round=0
# while N!=1:
#     round+=1
#     print(t)
#     t2=[]
#     for i in range(0,len(t),2):
#         print(i,'asdfasdf')
#         if t[i]==K:
#             if t[i+1]==L:
#                 print(round)
#                 sys.exit()
#             else:
#                 t2.append(t[i])
#                 print(111,t[i])
#                 continue
                
#         if i+1<len(t):
#             if t[i+1]==K:
#                 t2.append(t[i+1])
#                 print(2222,t[i+1])
#                 continue
#         if i+1<len(t):
#             if t[i+1]==L:
#                 t2.append(t[i+1])
#                 print(3333,t[i+1])
#                 continue
#         else:
#             continue
#         t2.append(t[i])
#         print(444,t[i])


#     if len(t)%2==1:
#         t2.append(t[-1])
#     t=t2
#     N=N//2

# print(-1)

n,start,end=map(int, input().split())
cnt=0
while start!=end:
  start -= start//2
  end -= end//2
  cnt+=1
print(cnt)