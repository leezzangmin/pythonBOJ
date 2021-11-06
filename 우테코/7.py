def solution(grid, clockwise):
    if clockwise:
        left,right,bottom=[],[],[]
        mid=[]
        for j in range(len(grid[-1])):
            if j%2==0:
                left.append(grid[-1][j]) #왼쪽
        for i in range(len(grid)):
            right.append(grid[i][0])

            for j in range(len(grid[i])):
                if j%2==1:
                    mid.append(grid[i][j])
            bottom.append(grid[i][-1])
        print(left,'l')
        right=right[::-1]
        print(right,'r')
        bottom=bottom[1:len(bottom)-1]
        print(bottom,'b')
        
        
        mid=mid[1:]+mid[0:1]
        print(mid,'m')

        temp=list([] for _ in range(len(grid)))
        print(temp)
        temp[0]+=left[0]
        for i in range(1,len(grid)):
            temp[i]+=left[i]
            for j in range(len(grid[i])):
                if j%2==1:
                    temp[i]+=mid.pop(0)
            temp[i]+=right[i]
        # if grid[i]==grid[-1]:
        #     while bottom:
        #         temp[i][i%2]=bottom.pop()
            print(temp)
    else:
        for i in range(2):
            left,right,bottom=[],[],[]
            mid=[]
            for j in range(len(grid[-1])):
                if j%2==0:
                    left.append(grid[-1][j]) #왼쪽
            for i in range(len(grid)):
                right.append(grid[i][0])

                for j in range(len(grid[i])):
                    if j%2==1:
                        mid.append(grid[i][j])
                bottom.append(grid[i][-1])
            print(left,'l')
            right=right[::-1]
            print(right,'r')
            bottom=bottom[1:len(bottom)-1]
            print(bottom,'b')
            
            
            mid=mid[1:]+mid[0:1]
            print(mid,'m')

            temp=list([] for _ in range(len(grid)))
            print(temp)
            temp[0]+=left[0]
            for i in range(1,len(grid)):
                temp[i]+=left[i]
                for j in range(len(grid[i])):
                    if j%2==1:
                        temp[i]+=mid.pop(0)
                temp[i]+=right[i]
            # if grid[i]==grid[-1]:
            #     while bottom:
            #         temp[i][i%2]=bottom.pop()
                grid=temp  

 
    return temp

a=["1","234","56789"]	
b=True
c=["5","762","98431"]


d=["A",
  "MAN",
 "DRINK",
"WATER11"]
f=["1",
  "K1R",
 "NNIET",
"AAMRDAW"]	
e=False
solution(a,c)

#   1     5
#  234   762
# 56789 98431