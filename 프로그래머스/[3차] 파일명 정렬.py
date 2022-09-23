def solution(files):
    lf=len(files)
    if lf<=1:
        return files
    else:
        
        ans=[['','',''] for _ in range(lf)] #head,number,tail,index

        for i in range(lf):
            lsf=len(files[i])
            #print(files[i],'files!')
            pointer=0
            while files[i][pointer].isdigit()==False:
                pointer+=1
            HEAD=files[i][0:pointer].lower()
         #   print(pointer,'pointer1')
            head_pointer=pointer
            while pointer!=lsf and files[i][pointer].isdigit() and pointer-head_pointer!=5:
                pointer+=1
        #    print(files[i],'fff',head_pointer,pointer)
        #    print(files[i][head_pointer:pointer],'asdf')
        #    print(int(files[i][head_pointer:pointer]),'bb')
        #    print(pointer,'pointer1')
            NUMBER=int(files[i][head_pointer:pointer])


            ans[i][0]=HEAD
            ans[i][1]=NUMBER
            ans[i][2]=i

        ans.sort(key=lambda x:(x[0],x[1],x[2]))
        ans2=[]
        for _,_,idx in ans:
            ans2.append(files[idx])
       # print(ans,'ans')
        return ans2






f=["img120011.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
f2=["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
f3=['A300001']
print(solution(f))
#print(solution(f2))
#print(solution(f3))
