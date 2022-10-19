n = 5
a = [list(map(int,input().split())) for _ in range(n)] # 2차원 리스트 입력

largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0 # 1은 행의 합, 2는 열의 합
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

sum1 = sum2 =  0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-1-i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2 
    
