from collections import defaultdict
def solution(info, query):
    answer = []
    for i in range(len(info)):
        info[i]=info[i].split()
    print(info)
    print(info.sort(key=lambda x:(x[0],x[1],x[2],x[3],x[4])))
    print(info)
    java_pointer=0
    python_pointer=0
    cpp_pointer=0

    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])