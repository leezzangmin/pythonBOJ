import sys;from itertools import combinations
input=sys.stdin.readline
N,K=map(int,input().split())
words=list(set(input().rstrip().replace('a','').replace('n','').replace('t','').replace('i','').replace('c','')) for _ in range(N))
bin_dict = {'b': 20, 'd': 19, 'e': 18, 'f': 17, 'g': 16, 'h': 15, 'j': 14,
            'k': 13, 'l': 12, 'm': 11, 'o': 10, 'p': 9, 'q': 8, 'r': 7,
            's': 6, 'u': 5, 'v': 4, 'w': 3, 'x': 2, 'y': 1, 'z': 0}
def word_to_bin(word):
    answer = 0b0
    for x in word:
        answer = answer | (1 << bin_dict[x])
    return answer


if K < 5:
    print(0)
else:
    bin_list = [word_to_bin(x) for x in words]
    max_count = 0

    # 2의 0제곱부터 2의 20제곱까지 저장한 리스트
    power_of_2 = [2 ** i for i in range(21)]

    # 현재 순회 중인 k - 5개의 알파벳 조합(comb)으로
    for comb in combinations(power_of_2, K - 5):
        current = sum(comb)
        count = 0
        for bin_number in bin_list:
            # 현재 순회 중인 단어를 만들 수 있다면
            if bin_number & current == bin_number:
                # count에 1을 더한다.
                count += 1

        # count = comb로 만들 수 있는 단어의 개수
        max_count = max(max_count, count)

    print(max_count)

































# import sys
# input=sys.stdin.readline
# N,K=map(int,input().split())
# words=list(input().rstrip() for _ in range(N))
# K=K-5
# teach=[]

# for i in range(N):
#     words[i]=list(set(words[i].replace('a','').replace('n','').replace('t','').replace('i','').replace('c','')))
    
# words.sort(key=lambda x:len(x))
# print(words)
# ans=0
# for i in range(N):
#     for j in range(len(words[i])):
#         if K<=0:
#             break
#         K-=1
#         print(i,j)
#         temp=words[i][0]
#         for g in range(N):
#             try:
#                 words[g].remove(temp)
#             except:
#                 pass
#     print(words)


# for i in range(N):
#     if not words[i]:
#         ans+=1
# print(ans)
