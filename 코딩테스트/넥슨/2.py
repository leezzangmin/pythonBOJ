

def sub(source_list,target_):
    global ls
    global lt
    pointer=0
    for i in range(lt):
        c=target_[i]
        if pointer>=ls:
           # print("FAlse!awsdjhfiawjureito")
            return False
        for j in range(pointer,ls):
          #  print(source_list[j],'sourceChar')
            if source_list[j]==c:
                pointer=j+1
                break
            if j>=ls-1 and source_list[j]!=c:
                return False
        #pointer=j

    return True


def getMaximumRemovals(order, source, target):
    global ls
    global lt
    answer=0    
    source=list(source)
    ls=len(source)
    lt=len(target)
    for i in order:
        source[i-1]=''
      #  print("".join(source),'string')
      #  print(source,target,'truefalse')
        if sub(source,target):
            answer+=1
            continue
        else:
            break

    return answer

print(getMaximumRemovals([7,1,2,5,4,3,6],"abbabaa","bb"))

#print(sub(['', '', 'b', 'a', 'b', 'a', ''],'bb'))