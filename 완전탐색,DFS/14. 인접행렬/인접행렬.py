# 무방향 그래프
n,m = map(int,input().split())
g = [[0]*(n+1) for _ in range(n+1)] # 0~5까지 ㅇㅇ
for i in range(m):
    a,b,c = map(int,input().split())
    g[a][b] = c
    g[b][a] = c
for i in range(1, n+1): # 1~5
    for j in range(1,n+1): # 1~5
        print(g[i][j],end = ' ')
    print()