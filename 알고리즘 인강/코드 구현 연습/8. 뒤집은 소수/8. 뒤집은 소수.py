n = int(input())
a = list(map(int,input().split()))

def reverse(x):
    res = 0
    while x>0:    # 숫자 교환 알고리즘
        t = x%10
        res= res*10 +t
        x = x//10
    return res

    
def isprime(x):
    if x == 1:      # 소수인지 판단하는 알고리즘
        return False
    for i in range(2,x//2+1):  # x의 약수는 절반을 넘을 수 없음
        if x%i == 0:
            return False
    else:
        return True
    
for x in a:
    tmp = reverse(x)
    if isprime(tmp):
        print(tmp, end =' ')
       