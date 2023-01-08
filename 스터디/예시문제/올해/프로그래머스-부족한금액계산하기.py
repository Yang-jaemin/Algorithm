# https://school.programmers.co.kr/learn/courses/30/lessons/82612\
    
def solution(price, money, count):
    total = 0
    for i in range(1,count+1):
        total += price*i
    if money >= total:
        answer = 0
    else:
        answer = total - money

    return answer



def solution(price, money, count):
    c = (count * (count + 1)) / 2 * price - money
    return 0 if c < 0 else c

    if c < 0:
        return 0
    else:
        return c