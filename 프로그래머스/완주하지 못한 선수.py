def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        print(i)
        if participant[i]!=completion[i]:
            return participant[i]
    return participant[-1]

    #return participant[0]


a=["marina", "josipa", "nikola", "vinko", "filipa"]
b=["josipa", "filipa", "marina", "nikola"]
a.sort()
b.sort()
print(a)
print(b)
print(solution(a,b))