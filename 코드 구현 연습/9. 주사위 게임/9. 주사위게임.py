n = int(input())

res = 0                 # 최댓값 계산 위함

for i in range(n):        # for문으로 3*3 개받음
    tmp = input().split() # string으로 받음
    tmp.sort()            # 정렬
    a,b,c = map(int,tmp)  # a,b,c에 맵핑
    if a==b and a==c:     # 세가지 다 같음
        money = 10000+(a*1000)
    elif a==b or a==c:    # 두개 같음 a포함만
        money = 1000 + (a*100)
    elif b==c:            # 두개 같음 bc
        money = 1000 + (b*100)
    else:                 # 안같음
        money = a*100
    
    if money > res:
        res = money

print(res)