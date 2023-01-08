# https://school.programmers.co.kr/learn/courses/30/lessons/49993
# ??분
def solution(skill, skill_trees):
    skill = list(skill)
    index_check= 0
    bb = False
    answer = 0
    for i in skill_trees:
        index_check = 0
        for j in range(len(i)):
            if i[j] in skill:
                tmp = skill.index(i[j])
                
                if tmp > index_check:
                    break
                elif tmp == index_check:
                    index_check += 1
            if j == len(i)-1:
                bb = True
        if bb:
            answer += 1
            bb = False
                
                
    return answer


def solution(skill, skill_trees):
    skill = list(skill)
    index_check= 0
    answer = 0
    for i in skill_trees:
        bb = True
        index_check = 0
        for j in range(len(i)):
            if i[j] in skill:
                tmp = skill.index(i[j])
                
                if tmp > index_check:
                    bb = False
                    break
                elif tmp == index_check:
                    index_check += 1
        if bb:
            answer += 1
                
                
    return answer



def sol(skill, skill_tree):
    for s in skill_tree:
        pos = skill.find(s)
        if pos == -1:
            continue
        elif pos == 0:
            skill = skill[1:]
        else:
            return 0
    return 1

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        answer += sol(skill, skill_tree)
    return answer