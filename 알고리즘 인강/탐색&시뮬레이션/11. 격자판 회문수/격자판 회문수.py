a = [list(map(int,input().split())) for _ in range(7)] # 7x7
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = a[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(5//2):
            if a[i+k][j] != a[i+k+4][j]:
                break
            else:
                cnt+=1
                
