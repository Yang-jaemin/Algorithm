n = int(input())
a = [list(map(int,input().split())) for _ in range(n)] # 5x5
m = int(input())
s = 0
e = n-1
total = 0
for i in range(m):
    h,t,k = map(int,input().split())
    if t == 0:
        for _ in range(k): # k만큼 회전(왼)
            a[h-1].append(a[h-1].pop(0)) # 0번 인덱스 빼서 뒤에 붙임 그러면 자동으로 1번 인덱스가 0번인덱스로 되어서 for문 돌리면댐
    else:
        for _ in range(k):
            a[h-1].insert(0,a[h-1].pop()) # 그냥 pop하면 맨 뒤에꺼 뺌 그리고 0번 인덱스에 집어넣으면 자동으로 밀림
for i in range(n):
    for j in range(s,e+1):
        total += a[i][j]
    if i < n//2: # 가운데 넘을때
        s = s+1
        e = e-1
    else:
        s = s-1
        e = e+1
        
            
        