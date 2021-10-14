s=input()
N=len(s)
i=0
ans=0
while i!=N:
    if s[i]=='c':
        if (i+1)<N:
            if s[i+1]=='=':
                ans+=1
                i+=2
                continue
            elif s[i+1]=='-':
                ans+=1
                i+=2
                continue
            else:
                ans+=1
                i+=1
                continue
        else:
            ans+=1
            i+=1
            continue

    elif s[i]=='d':
        if (i+1)<N:
            if s[i+1]=='z' and i+2<N and s[i+2]=='=':
                ans+=1
                i+=3
                continue
            elif s[i+1]=='-':
                ans+=1
                i+=2
                continue
            else:
                ans+=1
                i+=1
                continue
        else:
            ans+=1
            i+=1
            continue
    
    elif s[i]=='l':
        if (i+1)<N:
            if s[i+1]=='j':
                ans+=1
                i+=2
                continue
            else:
                ans+=1
                i+=1
                continue
        else:
            ans+=1
            i+=1
            continue
    
    elif s[i]=='n':
        if (i+1)<N:
            if s[i+1]=='j':
                ans+=1
                i+=2
                continue
            else:
                ans+=1
                i+=1
                continue
        else:
            ans+=1
            i+=1
            continue
    
    elif s[i]=='s':
        if (i+1)<N:
            if s[i+1]=='=':
                ans+=1
                i+=2
                continue
            else:
                ans+=1
                i+=1
                continue
        else:
            ans+=1
            i+=1
            continue
    
    elif s[i]=='z':
        if (i+1)<N:
            if s[i+1]=='=':
                ans+=1
                i+=2
                continue
            else:
                ans+=1
                i+=1
                continue
        else:
            ans+=1
            i+=1
            continue
    else:
        ans+=1
        i+=1
print(ans)