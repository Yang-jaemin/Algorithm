# 에라토스테네스의 채

for i in range(2,n+1): # 2부터 시작, 2는 소수니까 cnt +1
    if ch[i] == 0:
        cnt += 1
        for j in range(i,n+1,i): # range(i,n+1,i) 3번째 인자는 스텝인데 i만큼 증가하는거임
            ch[j] = 1
            
# 소수인지 판단하기

def isprime(x):
    if x == 1:      # 소수인지 판단하는 알고리즘
        return False
    for i in range(2,x//2+1):  # x의 약수는 절반을 넘을 수 없음
        if x%i == 0:
            return False
    else:
        return True