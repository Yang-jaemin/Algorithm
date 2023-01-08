s = 'g0n2T8e'
arr = ''
cnt = 0
for i in s:
    if i.isdigit():
        arr += i
    
else:   
    for j in range(1,int(arr)+1):
            if int(arr) % j == 0:
                cnt += 1        
               
               
print(cnt)

    