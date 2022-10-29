n = 5
largest = -2147000000
a = [list(map(int,input().split())) for _ in range(5)]
sum1 = sum2 = 0
for i in range(n):
    for j in range(n):
        sum1 = sum2 = 0
        sum1 += a[i][j]
        sum2 += a[j][i]
    if largest < sum1:
        largest = sum1
    if largest < sum2:
        largest = sum2
        # 대각선
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-1-i]
if largest < sum1:
        largest = sum1
if largest < sum2:
        largest = sum2
    
    
        