s=input().upper()
alphabet=[0]*26
ans=0

for i in s:
    alphabet[ord(i)-65]+=1

m=max(alphabet)
c=chr(alphabet.index(m)+65)

temp=0
for i in alphabet:
    if i==m:
        temp+=1
if temp!=1:
    print("?")
else:
    print(c)
