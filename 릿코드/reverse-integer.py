x=-1200
def reverse( x: int) -> int:

    a=str(x)
    if x<0:
        a="".join(reversed(a[1:]))
    else:
        a="".join(reversed(a))

    i=0
    while i!=len(a) and a[i]=='0' :
        i+=1
    if len(a)-i==0:
        return 0

    if int(a)>pow(2,31)-1 or int(a)<-pow(2,31):
        return 0 
    if x<0:
        
        return "-"+a[i:]
    else:
        return a[i:]
print( reverse(x))
