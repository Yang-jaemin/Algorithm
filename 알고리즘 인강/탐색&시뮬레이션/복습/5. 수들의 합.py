lt = 0
rt = 1
a = [1,2,1,3,1,1,1,2]
n = 8
m = 3
total = a[0]
cnt = 0

while True:
    if total < m:
        if rt < n:
            total+= a[rt]
            rt += 1
        else:
            break
    elif total == m:
        cnt += 1
        total -= a[lt]
        lt += 1
    else: 
        total -= a[lt]
        
    
