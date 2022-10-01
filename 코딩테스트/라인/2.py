from typing import List
from collections import defaultdict
import re


def solution(k: int, dic: List[str], chat: str) -> str:
    answer = ''
   # globalS=''

    d=defaultdict()
    for i in range(len(dic)):
        d[dic[i]]=True

    chat=chat.split(' ')
    # for c in dic:
    #     globalS+='(' + c.replace('.','.'+str({1,k}).replace(' ','')) + ')*'
    # globalS='('+globalS+')+'
        #globalS+='\n'
   # print(globalS,'globalS')

    lc=len(chat)
    for c in range(lc):
        if chat[c] in d:
            chat[c]='#'*len(chat[c])
        else:
            s='(' + chat[c].replace('.','.'+str({1,k}).replace(' ','')) + ')+'
            # p=re.compile(globalS)
            # iteration=re.finditer(p,chat[c])
            # for it in iteration:
            #     chat[c]=list(chat[c])
            #     chat[c][it.start():it.end()]='#'*(it.end()-it.start())
            #     chat[c]="".join(chat[c])
            p=re.compile(s)
            for word in dic:
                if p.fullmatch(word):
                    chat[c]='#'*len(chat[c])




    #print(chat)
    return " ".join(chat)
print(solution(2, ["slang", "badword"], "b... ab.cd bad.ord .word sl.. bad.word"))
#solution(3, ["abcde", "cdefg", "efgij"], ".. ab. cdefgh .gi. .z.")
