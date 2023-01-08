n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

# 상하좌우 비교할때 리스트 초기화
dx = [-1,0,1,0] #외우기
dy = [0,1,0,-1]

cnt = 0
# 가장자리 채워주기
a.insert(0,[0] * n) # 맨 위행
a.append([0] * n) # 맨 밑행
for x in a:
    x.insert(0,0) # 맨 왼열
    x.append(0) # 맨 오열
    
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)): # all() : ()이 모두 참이 되어야 참
            cnt += 1
print(cnt)
    