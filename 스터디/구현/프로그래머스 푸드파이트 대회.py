from collections import deque
food = [1,7,1,2]
def solution(food):
    table = deque(['0'])
    for i in range(len(food)-1,0,-1):
        food_i = food[i]//2
        for j in range(food_i):
            table.append(str(i))
            table.appendleft(str(i))        
    answer = ''.join(table)
    return answer