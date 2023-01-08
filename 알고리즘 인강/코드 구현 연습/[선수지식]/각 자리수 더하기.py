# 각 자리수 더하기
def digit_sum(x):
    sum = 0
    
    while x > 0:
         sum = sum + x%10 # 125 % 10 = 5   # 12 % 10 = 2    # 1 % 10 == 1
         x = x // 10      # 125 // 10 = 12 # 12 // 10 = 1
    return sum
    
    for i in str(x):   # 125를  '1' '2' '5' 의 스트링으로 받아서 각자리의 합을 구한다.
        sum = sum + int(i)
    return sum
# 숫자교환 알고리즘
def reverse(x):
    res = 0
    while x>0:    # 숫자 교환 알고리즘
        t = x%10
        res= res*10 +t
        x = x//10
    return res