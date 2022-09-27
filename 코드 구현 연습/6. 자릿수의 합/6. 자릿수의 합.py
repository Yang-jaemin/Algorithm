n = map(int,input())
a = list(map(int,input().split()))
max = 0 # 최댓값 구해야하니까 max 변수 필요

# 각 자리수를 더하는 법

def digit_sum(x):
    sum = 0
    
    # while x > 0:
    #     sum = sum + x%10 # 125 % 10 = 5   # 12 % 10 = 2    # 1 % 10 == 1
    #     x = x // 10      # 125 // 10 = 12 # 12 // 10 = 1
    # return sum
    
    for i in str(x):   # 125를  '1' '2' '5' 의 스트링으로 받아서 각자리의 합을 구한다.
        sum = sum + int(i)
    return sum
        
        
        
for x in a:
    total = digit_sum(x)
    if total > max:         #최댓값 구하기
        max = total
        res = x
    
print(x)
    