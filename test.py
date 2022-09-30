S = set()
for _ in range(1):
    txt = input()
    tl = len(txt)
    ret = ''
    for i in range(tl):
        ret += txt[i]
        print(ret,'ret')
        S.add(ret)
print(S)