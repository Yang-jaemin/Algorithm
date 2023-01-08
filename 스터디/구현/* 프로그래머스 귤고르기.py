# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 되는데 시간초과

from itertools import permutations
def solution(k, tangerine):
    answer = 0
    cnt_list = [0]*(max(tangerine)+1)
    r_list = []
    for i in range(len(tangerine)):
        cnt_list[tangerine[i]] += 1
    
    for j in range(len(cnt_list)):
        if cnt_list[j] != 0:
            r_list.append(cnt_list[j])
    for q in range(1,len(r_list)+1):
        c_list = list(permutations(r_list,q))
        for m in range(len(c_list)):
            sc = sum(c_list[m])
            if k <= sc:
                answer = q
                return answer

# counter 사용
from collections import Counter
def solution(k, tangerine):
    answer = 0
    cnt = Counter(tangerine)  # Counter({3: 2, 2: 2, 5: 2, 1: 1, 4: 1})
    r_cnt = sorted(list(cnt.items()), key = lambda x : x[1] , reverse = True)
                    # {(3,2),(2,2),(5,2)...} , x[1]를 key로 내림차순으로 정렬
    for i in r_cnt:
        k -= i[1]   # 갯수를 뺀다 근데 i가 바뀌면 종류가 1개 늘어나는 거니까 answer += 1 이고
        answer += 1 # 만약 k가 음수나 0이 되면 그 종류에서 감당이 가능하다고 판단 종류 추가 x하고 answer 반환
        if k <= 0:
            break
    
    return answer



from collections import defaultdict

def solution(k, tangerine):
    # dict = {}
    # for v in tangerine:
    #     if v not in dict:
    #         dict[v] = 0
    #     dict[v] += 1
    dict = defaultdict(lambda : 0)
    for v in tangerine:
        dict[v] += 1
    l = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    answer = 0
    for _, cnt in l:
        if k > 0:
            answer += 1
            k -= cnt
        else:
            break
    return answer