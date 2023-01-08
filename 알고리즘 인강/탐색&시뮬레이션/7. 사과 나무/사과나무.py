n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
total = 0
s = e = n//2
for i in range(n):
    for j in range(s,e+1):
        total += a[i][j] #n//2
    if i < n//2: # 가운데 넘을때
        s = s-1
        e = e+1
    else:
        s = s+1
        e = e+1