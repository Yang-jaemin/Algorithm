# 잘 따라가보자 과정이해
n, m = 8, 3
a = [1,2,1,3,1,1,1,2]
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot = tot + a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
        
print(cnt)
