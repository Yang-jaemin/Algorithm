n = input()
f_n = n
cnt = 0
if int(n) <10:
    n = '0'+n
    while True:
        nn = str(int(n[0])+int(n[1]))
        if len(nn) == 1:
            n = n[1]+nn
        else:
            n = n[1]+nn[1]
        cnt += 1
        if int(f_n) == int(n):
            print(cnt)
            break    
    
else:
    while True:
        nn = str(int(n[0])+int(n[1]))
        if len(nn) == 1:
            n = n[1]+nn
        else:
            n = n[1]+nn[1]
        cnt += 1
        if f_n == n:
            print(cnt)
            break

# 다른 사람 코드
tmp = inp = int(input())
count = 0

while True:
    ten = tmp//10
    one = tmp%10
    res = ten + one
    count += 1
    tmp = int(str(tmp % 10) + str(res % 10))
 
    if (inp==tmp):
        break
print(count)