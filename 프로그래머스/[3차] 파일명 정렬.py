def solution(files):
    lf=len(files)
    ans=[['','',''] for _ in range(lf)] #head,number,index
    for i in range(lf):
        lsf=len(files[i])
        pointer=0
        while files[i][pointer].isdigit()==False:
            pointer+=1
        HEAD=files[i][0:pointer].lower()
        head_pointer=pointer
        while pointer!=lsf and files[i][pointer].isdigit() and pointer-head_pointer!=5:
            pointer+=1
        NUMBER=int(files[i][head_pointer:pointer])
        ans[i][0],ans[i][1],ans[i][2]=HEAD,NUMBER,i
        
    ans.sort(key=lambda x:(x[0],x[1],x[2]))
    ans2=[]
    for _,_,idx in ans:
        ans2.append(files[idx])
    return ans2






f=["img120011.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
f2=["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
f3=['A300001']
print(solution(f))
#print(solution(f2))
#print(solution(f3))
