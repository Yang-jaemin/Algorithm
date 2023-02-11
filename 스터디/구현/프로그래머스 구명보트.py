from collections import deque
def solution(people,limit):
    people.sort()
    people = deque(people)  
    cnt = 0
    while people:
        cnt += 1
        w = people.pop()
        while w <= limit and len(people) != 0 :
            if w + people[0] > limit:
                break
            else:
                w += people[0]
                people.popleft()
    return cnt
            
            

# from collections import deque 
# def solution(people, limit):
#     people.sort()
#     people = deque(people)
#     cnt = 0
#     while people:
#         if len(people) == 1: # 사람이 한명 남았을때
#             cnt += 1
#             break
            
#         if people[-1] + people[0] <= limit: # 가장 가벼운애랑 가장 무거운애랑 탔을 때 제한을 안넘는다?
#             people.pop()
#             people.popleft()
#             cnt += 1
            
#         else:
#             people.pop()
#             cnt += 1
            
#     return cnt